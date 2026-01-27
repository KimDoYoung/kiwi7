import ast
import os
import glob
from collections import defaultdict

def find_duplicates(directory):
    print(f"Analyzing {directory}...")
    definitions = defaultdict(list)
    
    # Get all python files
    files = glob.glob(os.path.join(directory, "*.py"))
    
    for file_path in files:
        if "__init__.py" in file_path:
            continue
            
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                tree = ast.parse(f.read(), filename=file_path)
            except Exception as e:
                print(f"Error parsing {file_path}: {e}")
                continue

        for node in tree.body:
            if isinstance(node, ast.Assign):
                # We expect simple assignments like VAR = { ... }
                if isinstance(node.value, ast.Dict):
                    # Check if keys are strings (which they should be for tr_cd maps)
                    for key, val in zip(node.value.keys, node.value.values):
                        if isinstance(key, ast.Constant) and isinstance(key.value, str):
                            tr_cd = key.value
                            # We suspect keys starting with 't' or 'C' or 'j' etc are tr_cds.
                            # In this codebase, they seem to be like 't8410', 'CTRP6548R', etc.
                            # Let's just collect ALL string keys from top-level dictionaries
                            # that look like they might be tr_cds (alphanumeric, usually > 3 chars)
                            if len(tr_cd) > 3:
                                definitions[tr_cd].append(os.path.basename(file_path))

    # Filter for duplicates
    duplicates = {k: v for k, v in definitions.items() if len(v) > 1}
    
    if not duplicates:
        print("No duplicates found.")
    else:
        print(f"Found {len(duplicates)} duplicates:")
        for tr_cd, locations in sorted(duplicates.items()):
            print(f"  {tr_cd}: {', '.join(locations)}")
            
    return duplicates

if __name__ == "__main__":
    base_dir = "/home/kdy987/work/kiwi7/backend/domains/stkcompanys/ls/models"
    print("--- REQUESTS ---")
    req_dups = find_duplicates(os.path.join(base_dir, "requests"))
    print("\n--- RESPONSES ---")
    res_dups = find_duplicates(os.path.join(base_dir, "responses"))
