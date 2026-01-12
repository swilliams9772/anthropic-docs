import os
import difflib

def get_files(directory):
    try:
        return {f for f in os.listdir(directory) if f.endswith('.md')}
    except FileNotFoundError:
        return set()

old_dir = "anthropic_docs_backup/anthropic_docs_md"
new_dir = "anthropic_docs/anthropic_docs_md"

old_files = get_files(old_dir)
new_files = get_files(new_dir)

added = new_files - old_files
removed = old_files - new_files
common = new_files & old_files

print(f"Analysis of changes:")
print(f"====================")
print(f"Old directory: {old_dir} ({len(old_files)} files)")
print(f"New directory: {new_dir} ({len(new_files)} files)")
print(f"")

if added:
    print(f"Added files ({len(added)}):")
    for f in sorted(added):
        print(f"  + {f}")
    print("")

if removed:
    print(f"Removed files ({len(removed)}):")
    for f in sorted(removed):
        print(f"  - {f}")
    print("")

modified = []
for f in common:
    old_path = os.path.join(old_dir, f)
    new_path = os.path.join(new_dir, f)
    
    with open(old_path, 'r', encoding='utf-8') as f1, open(new_path, 'r', encoding='utf-8') as f2:
        old_content = f1.read()
        new_content = f2.read()
        
    if old_content != new_content:
        modified.append(f)

if modified:
    print(f"Modified files ({len(modified)}):")
    for f in sorted(modified):
        print(f"  * {f}")
        
    print("\nDiff for first modified file:")
    first_mod = sorted(modified)[0]
    old_path = os.path.join(old_dir, first_mod)
    new_path = os.path.join(new_dir, first_mod)
    
    with open(old_path, 'r', encoding='utf-8') as f1, open(new_path, 'r', encoding='utf-8') as f2:
        old_lines = f1.readlines()
        new_lines = f2.readlines()
        
    diff = difflib.unified_diff(old_lines, new_lines, fromfile=f'old/{first_mod}', tofile=f'new/{first_mod}', n=2)
    for line in list(diff)[:20]:
        print(line, end='')
    print("...\n")
else:
    print("No content changes in common files.")


