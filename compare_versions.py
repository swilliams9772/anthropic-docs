import os
import difflib
import sys

def get_files(directory):
    try:
        return {f for f in os.listdir(directory) if f.endswith('.md')}
    except FileNotFoundError:
        return set()

def compare_dirs(old_dir, new_dir, old_label, new_label):
    print(f"Comparing {old_label} -> {new_label}")
    print(f"Old dir: {old_dir}")
    print(f"New dir: {new_dir}")
    
    old_files = get_files(old_dir)
    new_files = get_files(new_dir)
    
    added = new_files - old_files
    removed = old_files - new_files
    common = new_files & old_files
    
    print(f"Files in old: {len(old_files)}")
    print(f"Files in new: {len(new_files)}")
    
    if added:
        print(f"\nAdded files ({len(added)}):")
        for f in sorted(added)[:10]:
            print(f"  + {f}")
        if len(added) > 10:
            print(f"  ... and {len(added)-10} more")

    if removed:
        print(f"\nRemoved files ({len(removed)}):")
        for f in sorted(removed)[:10]:
            print(f"  - {f}")
        if len(removed) > 10:
            print(f"  ... and {len(removed)-10} more")

    modified = []
    significant_changes = []
    
    for f in common:
        old_path = os.path.join(old_dir, f)
        new_path = os.path.join(new_dir, f)
        
        try:
            with open(old_path, 'r', encoding='utf-8') as f1:
                old_content = f1.read()
            with open(new_path, 'r', encoding='utf-8') as f2:
                new_content = f2.read()
                
            if old_content != new_content:
                modified.append(f)
                
                # Check for significant changes (ignoring headers/footers if possible, or just size)
                # Simple heuristic: if size changed by > 5%
                if abs(len(old_content) - len(new_content)) / max(len(old_content), 1) > 0.05:
                    significant_changes.append(f)
                    
        except Exception as e:
            print(f"Error comparing {f}: {e}")

    if modified:
        print(f"\nModified files ({len(modified)}):")
        # Show significant ones first
        for f in sorted(significant_changes):
            print(f"  * {f} (significant change)")
        
        for f in sorted(list(set(modified) - set(significant_changes)))[:10]:
            print(f"  * {f}")
        if len(modified) - len(significant_changes) > 10:
            print(f"  ... and {len(modified) - len(significant_changes) - 10} others")

    print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    # Compare Aug vs Now
    compare_dirs(
        "anthropic_docs_prev_20250814_145715/anthropic_docs_md",
        "anthropic_docs/anthropic_docs_md",
        "Aug 14 2025",
        "Nov 23 2025 (Current)"
    )


