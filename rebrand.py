"""Rebrand script: ApplyPilot/Pickle-Pixel -> promelia/ryzalain.

Reads all files first, then writes. Case-sensitive replacements.
"""

import os

ROOT = "c:/Users/Lain/Documents/promelia"
EXTS = ('.py', '.md', '.yaml', '.yml', '.json', '.txt', '.toml')
SPECIAL_FILES = ('.env.example',)

# Collect all target files
files = []
for dp, dn, fns in os.walk(ROOT):
    # Skip .git directory
    if '.git' in dp.split(os.sep):
        continue
    for f in fns:
        path = os.path.join(dp, f)
        if f == 'rebrand.py':
            continue
        if any(f.endswith(ext) for ext in EXTS) or f in SPECIAL_FILES:
            files.append(path)

# Define replacements in order (order matters!)
replacements = [
    # 1. GitHub username
    ('Pickle-Pixel', 'ryzalain'),
    # 2. CamelCase program name
    ('ApplyPilot', 'Promelia'),
    # 3. Lowercase package/CLI references
    ('applypilot', 'promelia'),
    # 4. Environment variable prefix
    ('APPLYPILOT_DIR', 'PROMELIA_DIR'),
]

# Phase 1: Read all, replace, write back
total_changed = 0
for path in files:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
    except (UnicodeDecodeError, PermissionError):
        continue

    original = content
    for old, new in replacements:
        content = content.replace(old, new)

    if content != original:
        with open(path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print(f"  Updated: {os.path.relpath(path, ROOT)}")
        total_changed += 1

print(f"\nPhase 1 complete: {total_changed} files updated.")

# Phase 2: Fix casing - in Python files, imports/paths need lowercase 'promelia' not 'Promelia'
py_replacements = [
    ('from Promelia.', 'from promelia.'),
    ('from Promelia ', 'from promelia '),
    ('import Promelia', 'import promelia'),
    ('python -m Promelia', 'python -m promelia'),
    ('~/.Promelia', '~/.promelia'),
    ("'.Promelia'", "'.promelia'"),
    ('".Promelia"', '".promelia"'),
]

phase2_changed = 0
for path in files:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
    except (UnicodeDecodeError, PermissionError):
        continue

    original = content
    for old, new in py_replacements:
        content = content.replace(old, new)

    if content != original:
        with open(path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print(f"  Fixed casing: {os.path.relpath(path, ROOT)}")
        phase2_changed += 1

print(f"\nPhase 2 complete: {phase2_changed} files fixed.")

# Phase 3: Rename directory
old_dir = os.path.join(ROOT, 'src', 'applypilot')
new_dir = os.path.join(ROOT, 'src', 'promelia')
if os.path.exists(old_dir):
    os.rename(old_dir, new_dir)
    print(f"\nRenamed: src/applypilot -> src/promelia")
elif os.path.exists(new_dir):
    print(f"\nsrc/promelia already exists (already renamed)")
else:
    print(f"\nWARNING: Neither src/applypilot nor src/promelia found!")

print("\n✅ Rebranding complete!")
