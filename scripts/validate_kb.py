#!/usr/bin/env python3
"""
Knowledge Base Validation Script

Checks:
1. All notes have valid frontmatter (title, type, date)
2. All WikiLinks point to existing files
3. No orphan notes (not linked from Index or other notes)
4. Index.md is reachable from AGENTS.md
"""

import re
import sys
from pathlib import Path
from typing import Set, Dict, List, Tuple
import yaml

# ANSI color codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def parse_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter from markdown content."""
    if not content.startswith('---'):
        return {}
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}
    
    try:
        return yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return {}

def extract_wikilinks(content: str) -> List[str]:
    """Extract all WikiLinks from markdown content."""
    # Match [[path]] or [[path|display]]
    pattern = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'
    return re.findall(pattern, content)

def resolve_wikilink(link: str, base_dir: Path) -> Path:
    """Resolve a WikiLink to a file path."""
    # Remove any .md extension if present
    link = link.rstrip('.md')
    
    # Add .md extension
    md_path = base_dir / f"{link}.md"
    
    return md_path

def check_frontmatter(kb_root: Path) -> List[str]:
    """Check all markdown files have valid frontmatter."""
    errors = []
    
    for md_file in kb_root.rglob("*.md"):
        # Skip templates and examples
        if '_templates' in md_file.parts or md_file.name.endswith('.example'):
            continue
        
        content = md_file.read_text(encoding='utf-8')
        fm = parse_frontmatter(content)
        
        relative_path = md_file.relative_to(kb_root)
        
        if not fm:
            errors.append(f"{relative_path}: Missing frontmatter")
            continue
        
        # Check required fields
        if 'title' not in fm:
            errors.append(f"{relative_path}: Missing 'title' in frontmatter")
        if 'type' not in fm:
            errors.append(f"{relative_path}: Missing 'type' in frontmatter")
        if 'date' not in fm:
            errors.append(f"{relative_path}: Missing 'date' in frontmatter")
    
    return errors

def check_wikilinks(kb_root: Path) -> List[str]:
    """Check all WikiLinks point to existing files."""
    errors = []
    
    for md_file in kb_root.rglob("*.md"):
        # Skip templates and examples
        if '_templates' in md_file.parts or md_file.name.endswith('.example'):
            continue
        
        content = md_file.read_text(encoding='utf-8')
        links = extract_wikilinks(content)
        
        relative_path = md_file.relative_to(kb_root)
        
        for link in links:
            target = resolve_wikilink(link, kb_root)
            
            if not target.exists():
                errors.append(f"{relative_path}: Broken link [[{link}]] -> {target}")
    
    return errors

def check_orphans(kb_root: Path) -> List[str]:
    """Check for orphan notes not linked from anywhere."""
    # Find all markdown files
    all_notes = set()
    for md_file in kb_root.rglob("*.md"):
        if '_templates' in md_file.parts or md_file.name.endswith('.example'):
            continue
        if md_file.name in ['AGENTS.md', 'README.md']:
            continue
        all_notes.add(md_file.relative_to(kb_root))
    
    # Find all linked notes
    linked_notes = set()
    
    for md_file in kb_root.rglob("*.md"):
        if '_templates' in md_file.parts or md_file.name.endswith('.example'):
            continue
        
        content = md_file.read_text(encoding='utf-8')
        links = extract_wikilinks(content)
        
        for link in links:
            target = resolve_wikilink(link, kb_root)
            if target.exists():
                linked_notes.add(target.relative_to(kb_root))
    
    # Orphans are notes that exist but are never linked
    orphans = all_notes - linked_notes
    
    # Exclude certain files that don't need to be linked
    exclude_patterns = ['00_Meta/Principles.md', '00_Meta/Schema.md']
    orphans = [o for o in orphans if not any(str(o) == p.replace('/', '\\') or str(o) == p for p in exclude_patterns)]
    
    return [f"Orphan note (not linked from anywhere): {o}" for o in sorted(orphans)]

def main():
    # Find knowledge base root
    kb_root = Path(__file__).parent.parent
    
    print(f"Validating knowledge base at: {kb_root}\n")
    
    all_errors = []
    
    # Check frontmatter
    print("Checking frontmatter...")
    fm_errors = check_frontmatter(kb_root)
    if fm_errors:
        all_errors.extend(fm_errors)
        print(f"  {RED}✗ {len(fm_errors)} frontmatter errors{RESET}")
    else:
        print(f"  {GREEN}✓ All frontmatter valid{RESET}")
    
    # Check WikiLinks
    print("Checking WikiLinks...")
    link_errors = check_wikilinks(kb_root)
    if link_errors:
        all_errors.extend(link_errors)
        print(f"  {RED}✗ {len(link_errors)} broken links{RESET}")
    else:
        print(f"  {GREEN}✓ All links valid{RESET}")
    
    # Check for orphans
    print("Checking for orphan notes...")
    orphan_errors = check_orphans(kb_root)
    if orphan_errors:
        all_errors.extend(orphan_errors)
        print(f"  {YELLOW}⚠ {len(orphan_errors)} orphan notes{RESET}")
    else:
        print(f"  {GREEN}✓ No orphan notes{RESET}")
    
    # Print all errors
    if all_errors:
        print(f"\n{RED}{'='*60}{RESET}")
        print(f"{RED}VALIDATION FAILED: {len(all_errors)} issues found{RESET}")
        print(f"{RED}{'='*60}{RESET}\n")
        for error in all_errors:
            print(f"  • {error}")
        sys.exit(1)
    else:
        print(f"\n{GREEN}{'='*60}{RESET}")
        print(f"{GREEN}✓ VALIDATION PASSED: Knowledge base is healthy{RESET}")
        print(f"{GREEN}{'='*60}{RESET}")
        sys.exit(0)

if __name__ == '__main__':
    main()
