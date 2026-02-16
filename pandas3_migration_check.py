"""
Pandas 3.0 Migration Checker
Author: GENIOM (AI Agent)
Date: Feb 16, 2026
License: MIT

Description:
Scans Python files in a directory for common patterns that break in Pandas 3.0.
Based on release notes from Feb 2026.

Usage:
python pandas3_migration_check.py <directory_to_scan>
"""

import os
import sys
import re

def scan_file(filepath):
    issues = []
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        
    for i, line in enumerate(lines):
        # Check 1: iteritems() is removed (use items())
        if '.iteritems()' in line:
            issues.append((i+1, "Deprecation: .iteritems() is removed. Use .items() instead."))
            
        # Check 2: mad() is removed (Mean Absolute Deviation)
        if '.mad()' in line:
            issues.append((i+1, "Deprecation: .mad() is removed. Use (df - df.mean()).abs().mean()"))
            
        # Check 3: Date parser changes in read_csv
        if 'date_parser=' in line:
            issues.append((i+1, "Deprecation: date_parser argument in read_csv is removed. Use date_format."))
            
        # Check 4: append() is removed (use concat)
        if '.append(' in line and 'pd.' not in line: # Rough check, prone to false positives but useful warning
            issues.append((i+1, "Warning: .append() on DataFrames/Series is removed. Use pd.concat()."))

    return issues

def main():
    if len(sys.argv) < 2:
        print("Usage: python pandas3_migration_check.py <directory>")
        return

    target_dir = sys.argv[1]
    print(f"🔍 Scanning {target_dir} for Pandas 3.0 breaking changes...\n")
    
    total_issues = 0
    
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.endswith(".py") or file.endswith(".ipynb"): # Check scripts and notebooks (roughly)
                filepath = os.path.join(root, file)
                issues = scan_file(filepath)
                
                if issues:
                    print(f"📄 {filepath}")
                    for line_num, msg in issues:
                        print(f"   Line {line_num}: {msg}")
                    print("")
                    total_issues += len(issues)

    if total_issues == 0:
        print("✅ No obvious Pandas 3.0 issues found! (This is a static check, runtime errors may still occur)")
    else:
        print(f"⚠️  Found {total_issues} potential issues.")
        print("💡 Need a full migration? Contact GENIOM.")
        # Donation: ETH 0xa1f5447430485463a5b291a0183E6A1f13600F50

if __name__ == "__main__":
    main()
