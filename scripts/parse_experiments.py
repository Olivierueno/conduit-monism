#!/usr/bin/env python3
"""
Parse experiment markdown files and extract individual tests/experiments.

Some files contain multiple tests (e.g., Falsification Suite has 7 tests).
This script separates them and creates a structured JSON index.
"""

import json
import re
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional

EXPERIMENTS_DIR = Path(__file__).parent.parent / "experiments"
OUTPUT_DIR = Path(__file__).parent.parent / "website" / "public" / "data"


def extract_tests_from_markdown(content: str, filename: str) -> List[Dict]:
    """
    Extract individual tests from a markdown file.
    
    Looks for patterns like:
    - ## Test N: Title
    - ### Test N: Title
    - ## Experiment: Title
    """
    tests = []
    
    # Check if this is a multi-test file (Falsification Suite, Break Tests, etc.)
    if "Test 1:" in content or "Test 2:" in content or "## Test" in content:
        # Split by test markers
        test_pattern = r'##\s+Test\s+(\d+):\s+(.+?)(?=##\s+Test\s+\d+:|##\s+[^T]|$)'
        matches = re.finditer(test_pattern, content, re.DOTALL)
        
        for match in matches:
            test_num = match.group(1)
            test_content = match.group(2).strip()
            title_match = re.search(r'^(.+?)(?:\(|$)', match.group(2).strip().split('\n')[0])
            title = title_match.group(1).strip() if title_match else f"Test {test_num}"
            
            tests.append({
                'id': f"{filename}_test_{test_num}",
                'title': title,
                'content': test_content,
                'parent_file': filename,
                'test_number': int(test_num)
            })
    
    # Check for other multi-experiment patterns
    elif "### Test" in content or "## Experiment" in content:
        # Try alternative patterns
        alt_pattern = r'##\s+Experiment[:\s]+(.+?)(?=##\s+Experiment|##\s+[^E]|$)'
        matches = re.finditer(alt_pattern, content, re.DOTALL)
        
        for i, match in enumerate(matches, 1):
            title = match.group(1).split('\n')[0].strip()
            test_content = match.group(0).strip()
            
            tests.append({
                'id': f"{filename}_exp_{i}",
                'title': title,
                'content': test_content,
                'parent_file': filename,
                'test_number': i
            })
    
    # If no multi-test pattern found, treat entire file as one experiment
    if not tests:
        # Extract title from first heading
        title_match = re.search(r'^#\s+(.+?)$', content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else filename.replace('.md', '').replace('_', ' ')
        
        tests.append({
            'id': filename.replace('.md', ''),
            'title': title,
            'content': content,
            'parent_file': filename,
            'test_number': None
        })
    
    return tests


def classify_experiment(content: str, filename: str) -> Dict:
    """
    Classify experiment by status and type.
    """
    content_lower = content.lower()
    
    # Determine status
    status = "completed"
    if "planned" in content_lower or "todo" in content_lower or "proposed" in content_lower:
        status = "planned"
    elif "falsified" in content_lower or "broken" in content_lower or "failed" in content_lower:
        status = "falsified"
    elif "confirmed" in content_lower or "passed" in content_lower or "✅" in content:
        status = "confirmed"
    elif "pending" in content_lower or "in progress" in content_lower:
        status = "pending"
    
    # Determine type
    exp_type = "validation"
    if "falsification" in content_lower:
        exp_type = "falsification"
    elif "binding" in content_lower or "amnesia" in content_lower:
        exp_type = "binding"
    elif "architecture" in content_lower or "chimera" in content_lower:
        exp_type = "architecture"
    elif "entropy" in content_lower or "coherence" in content_lower:
        exp_type = "formula"
    elif "animal" in content_lower or "species" in content_lower:
        exp_type = "comparative"
    
    # Extract date
    date_match = re.search(r'(\d{6})', filename)
    date_str = date_match.group(1) if date_match else None
    
    return {
        'status': status,
        'type': exp_type,
        'date': date_str
    }


def parse_all_experiments() -> Dict:
    """
    Parse all experiment files and create index.
    """
    experiments = []
    
    for md_file in sorted(EXPERIMENTS_DIR.glob("*.md")):
        try:
            content = md_file.read_text(encoding='utf-8')
            classification = classify_experiment(content, md_file.name)
            tests = extract_tests_from_markdown(content, md_file.name)
            
            for test in tests:
                experiments.append({
                    **test,
                    **classification,
                    'filename': md_file.name
                })
        except Exception as e:
            print(f"Error parsing {md_file.name}: {e}")
            continue
    
    # Organize by status
    organized = {
        'confirmed': [e for e in experiments if e['status'] == 'confirmed'],
        'falsified': [e for e in experiments if e['status'] == 'falsified'],
        'pending': [e for e in experiments if e['status'] == 'pending'],
        'planned': [e for e in experiments if e['status'] == 'planned'],
        'all': experiments
    }
    
    return organized


def main():
    """Generate experiment index JSON."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    organized = parse_all_experiments()
    
    # Save full index
    index_file = OUTPUT_DIR / "experiments_index.json"
    with open(index_file, 'w') as f:
        json.dump(organized, f, indent=2)
    
    print(f"Generated index with {len(organized['all'])} experiments")
    print(f"  - Confirmed: {len(organized['confirmed'])}")
    print(f"  - Falsified: {len(organized['falsified'])}")
    print(f"  - Pending: {len(organized['pending'])}")
    print(f"  - Planned: {len(organized['planned'])}")
    print(f"\nSaved to: {index_file}")


if __name__ == "__main__":
    main()
