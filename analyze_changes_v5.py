#!/usr/bin/env python3
"""
Analyze changes between two snapshots of the Anthropic documentation.

Outputs:
- Summary of added/removed/modified files
- Categorized lists of changes (by section)
- A short diff sample for the largest modifications
- Writes a machine-readable JSON report (changes_report.json)
- Writes a human-friendly markdown report (CHANGES_SUMMARY.md)

Compares: anthropic_docs_backup_20260109_151013 (Jan 9, 2026)
     vs : anthropic_docs                       (May 23, 2026 - current)
"""

from __future__ import annotations

import difflib
import json
import os
import re
from collections import defaultdict
from datetime import datetime

OLD_DIR = "anthropic_docs_backup_20260523_124122/anthropic_docs_md"
NEW_DIR = "anthropic_docs/anthropic_docs_md"

OLD_LABEL = "Jan 9, 2026 (previous scrape)"
NEW_LABEL = "May 23, 2026 (current scrape)"


def get_files(directory: str) -> set[str]:
    try:
        return {f for f in os.listdir(directory) if f.endswith(".md")}
    except FileNotFoundError:
        return set()


def categorize(filename: str) -> str:
    """Group a filename into a high-level doc section."""
    # Strip the en_ prefix
    name = filename[3:] if filename.startswith("en_") else filename
    name = name[:-3] if name.endswith(".md") else name

    # First path-segment-ish heuristic
    head = name.split("_", 1)[0]
    mapping = {
        "about-claude": "About Claude",
        "api": "API Reference",
        "build-with-claude": "Build with Claude",
        "agents-and-tools": "Agents & Tools",
        "agent-sdk": "Agent SDK",
        "claude-code": "Claude Code",
        "test-and-evaluate": "Test & Evaluate",
        "resources": "Resources",
        "release-notes": "Release Notes",
        "third-party-platforms": "Third-party Platforms",
        "articles": "Support Articles",
        "intro": "Intro",
        "home": "Home",
        "developer-platform": "Developer Platform",
        "managed-agents": "Managed Agents",
        "claude-haiku": "Claude Haiku",
        "claude-sonnet": "Claude Sonnet",
        "claude-opus": "Claude Opus",
    }
    return mapping.get(head, head.replace("-", " ").title())


def read_text(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return ""


def strip_source_line(text: str) -> str:
    """Remove the auto-injected '**Source:** ...' header line so it doesn't
    create noisy diffs that look like content changes when only URLs/dates moved."""
    return re.sub(r"^\*\*Source:\*\*.*\n", "", text, count=1, flags=re.MULTILINE)


def main() -> None:
    old_files = get_files(OLD_DIR)
    new_files = get_files(NEW_DIR)

    added = sorted(new_files - old_files)
    removed = sorted(old_files - new_files)
    common = new_files & old_files

    modified: list[tuple[str, int, int]] = []  # (filename, old_size, new_size)
    unchanged = 0
    for f in sorted(common):
        old_text = strip_source_line(read_text(os.path.join(OLD_DIR, f)))
        new_text = strip_source_line(read_text(os.path.join(NEW_DIR, f)))
        if old_text != new_text:
            modified.append((f, len(old_text), len(new_text)))
        else:
            unchanged += 1

    modified.sort(key=lambda t: abs(t[2] - t[1]), reverse=True)

    by_section_added: dict[str, list[str]] = defaultdict(list)
    for f in added:
        by_section_added[categorize(f)].append(f)
    by_section_removed: dict[str, list[str]] = defaultdict(list)
    for f in removed:
        by_section_removed[categorize(f)].append(f)
    by_section_modified: dict[str, list[str]] = defaultdict(list)
    for f, _, _ in modified:
        by_section_modified[categorize(f)].append(f)

    # ---- Print summary to stdout ------------------------------------------------
    print("=" * 72)
    print(f"Anthropic docs change report  ({OLD_LABEL} → {NEW_LABEL})")
    print("=" * 72)
    print(f"Old directory: {OLD_DIR}  ({len(old_files)} files)")
    print(f"New directory: {NEW_DIR}  ({len(new_files)} files)")
    print()
    print(f"Net change: {len(new_files) - len(old_files):+d} files "
          f"({len(added)} added, {len(removed)} removed, {len(modified)} modified, "
          f"{unchanged} unchanged)")
    print()

    def print_section(title: str, sections: dict[str, list[str]]) -> None:
        if not sections:
            return
        print(f"\n## {title}")
        for section in sorted(sections):
            files = sections[section]
            print(f"\n### {section} ({len(files)})")
            for f in files[:25]:
                print(f"  - {f}")
            if len(files) > 25:
                print(f"  ... and {len(files) - 25} more")

    print_section(f"Added files ({len(added)})", by_section_added)
    print_section(f"Removed files ({len(removed)})", by_section_removed)
    print_section(f"Modified files ({len(modified)})", by_section_modified)

    # ---- Sample diffs for biggest changes --------------------------------------
    print("\n" + "=" * 72)
    print("Top 5 biggest content changes (diff snippets)")
    print("=" * 72)
    for f, old_size, new_size in modified[:5]:
        print(f"\n--- {f}  ({old_size:,} → {new_size:,} chars, "
              f"{new_size - old_size:+,})")
        old_lines = strip_source_line(read_text(os.path.join(OLD_DIR, f))).splitlines(keepends=True)
        new_lines = strip_source_line(read_text(os.path.join(NEW_DIR, f))).splitlines(keepends=True)
        diff = list(difflib.unified_diff(
            old_lines, new_lines,
            fromfile=f"old/{f}", tofile=f"new/{f}", n=1,
        ))
        for line in diff[:60]:
            print(line.rstrip("\n"))
        if len(diff) > 60:
            print(f"... ({len(diff) - 60} more diff lines)")

    # ---- JSON report -----------------------------------------------------------
    report = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "old_snapshot": {"label": OLD_LABEL, "dir": OLD_DIR, "file_count": len(old_files)},
        "new_snapshot": {"label": NEW_LABEL, "dir": NEW_DIR, "file_count": len(new_files)},
        "counts": {
            "added": len(added),
            "removed": len(removed),
            "modified": len(modified),
            "unchanged": unchanged,
            "net_change": len(new_files) - len(old_files),
        },
        "added": added,
        "removed": removed,
        "modified": [
            {"file": f, "old_size": o, "new_size": n, "delta": n - o}
            for f, o, n in modified
        ],
        "by_section": {
            "added": {k: sorted(v) for k, v in by_section_added.items()},
            "removed": {k: sorted(v) for k, v in by_section_removed.items()},
            "modified": {k: sorted(v) for k, v in by_section_modified.items()},
        },
    }
    with open("changes_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print("\nWrote changes_report.json")


if __name__ == "__main__":
    main()
