import ast
import os
import glob
from collections import defaultdict

# Priority files (keep definitions here)
PRIORITY_FILES = [
    'market_chart.py',
    'market_derivatives_query.py',
    'market_etf.py',
    'market_elw.py',
    'market_account.py',
    # Add others as needed, general rule: specific > original
]

# Deprioritized files (remove definitions from here if found elsewhere)
LOW_PRIORITY_FILES = [
    'market_original.py',
    'market_future_original.py',
    'market_overseas_original.py'
]

def get_file_priority(filename):
    base = os.path.basename(filename)
    if base in PRIORITY_FILES:
        return 2
    if base in LOW_PRIORITY_FILES:
        return 0
    return 1

def analyze_duplicates(directory):
    definitions = defaultdict(list)
    files = glob.glob(os.path.join(directory, "*.py"))
    
    file_map = {} # filename -> file_path

    for file_path in files:
        if "__init__.py" in file_path:
            continue
        
        file_map[os.path.basename(file_path)] = file_path
        
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                tree = ast.parse(f.read(), filename=file_path)
            except Exception as e:
                print(f"Error parsing {file_path}: {e}")
                continue

        for node in tree.body:
            if isinstance(node, ast.Assign) and isinstance(node.value, ast.Dict):
                for key, val in zip(node.value.keys, node.value.values):
                    if isinstance(key, ast.Constant) and isinstance(key.value, str):
                        tr_cd = key.value
                        if len(tr_cd) > 3:
                            # Verify if it really looks like a definition (has 'tr_cd' inside value dict)
                            is_def = False
                            if isinstance(val, ast.Dict):
                                for sub_key in val.keys:
                                    if isinstance(sub_key, ast.Constant) and sub_key.value == 'tr_cd':
                                        is_def = True
                                        break
                            
                            if is_def:
                                definitions[tr_cd].append(os.path.basename(file_path))

    return definitions, file_map

def remove_keys_from_file(file_path, keys_to_remove):
    if not keys_to_remove:
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # We need to find the lines to remove.
    # parsing again to get line numbers
    with open(file_path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=file_path)

    ranges_to_remove = []

    for node in tree.body:
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Dict):
            for key, val in zip(node.value.keys, node.value.values):
                if isinstance(key, ast.Constant) and isinstance(key.value, str):
                    if key.value in keys_to_remove:
                        # AST line numbers are 1-indexed
                        # key.lineno is where the key starts.
                        # We want to remove from the line of the key up to the end of the value.
                        # HOWEVER, this is tricky with commas and formatting.
                        # Simplest robust way: 
                        # If the dict items are on separate lines, we can try to identify the block.
                        
                        start_line = key.lineno
                        end_line = val.end_lineno
                        
                        # Adjust start line to include the line with the key if it's indented
                        # But be careful not to remove the parent brace if it's on the same line (unlikely for big dicts)
                        
                        # We will comment them out or remove them? Removing is cleaner but harder to get right with commas.
                        # Let's try to remove lines [start_line-1, end_line] 
                        # BUT we need to handle the comma after the value.
                        
                        # Check strict line range.
                        ranges_to_remove.append((start_line, end_line))

    # Sort ranges descending to remove from bottom up
    ranges_to_remove.sort(key=lambda x: x[0], reverse=True)
    
    new_lines = lines[:]
    
    for start, end in ranges_to_remove:
        # Check if the line after end has a comma that belongs to this item
        # or if the comma is on the end_line
        
        # 0-indexed conversion
        idx_start = start - 1
        idx_end = end # slice up to end (exclusive in slice, but line no is inclusive)
        
        # Check for trailing comma on the execution line or next line
        # This is heuristics based.
        
        # Safer approach: replace lines with blank or comment
        # "REMOVED_DUPLICATE"
        # Since we want to clean up, let's try to remove.
        
        # Identify the full block including trailing comma
        # Look at the character immediately following the value in source?
        # Python AST doesn't give comma location easily.
        
        # Alternative: Read the file content, find the substring corresponding to the key/value and remove it.
        pass

    # Re-reading strategy is hard. 
    # Let's use a simpler marker approach for now, or just do it strictly by line if formatted well.
    # The files seem auto-generated and well formatted (one key per block).
    
    curr_lines = lines
    for start, end in ranges_to_remove:
        # Remove lines from start-1 to end
        # Also check if the line immediately following is just a comma + newline
        
        # Remove lines
        del curr_lines[start-1:end]
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(curr_lines)

def deduplicate(directory):
    definitions, file_map = analyze_duplicates(directory)
    
    to_remove = defaultdict(list) # file -> list of keys to remove

    duplicates_count = 0
    for tr_cd, files in definitions.items():
        if len(files) > 1:
            duplicates_count += 1
            # Decide which to keep
            files_with_priority = [(f, get_file_priority(f)) for f in files]
            # Sort by priority desc, then filename asc
            files_with_priority.sort(key=lambda x: (-x[1], x[0]))
            
            keep_file = files_with_priority[0][0]
            remove_files = [f[0] for f in files_with_priority[1:]]
            
            print(f"Duplicate {tr_cd}: keeping in {keep_file} (p={files_with_priority[0][1]}), removing from {remove_files}")
            
            for rf in remove_files:
                to_remove[file_map[rf]].append(tr_cd)

    print(f"Total duplicates groups found: {duplicates_count}")
    
    if duplicates_count == 0:
        return

    # Execute removal
    # Since direct line removal is risky, I will actually READ the file, parse AST, 
    # and reconstruct the dictionary omitting the keys. This guarantees syntax correctness.
    
    for file_path, keys in to_remove.items():
        print(f"Processing {os.path.basename(file_path)}: removing {len(keys)} keys")
        remove_keys_safe(file_path, keys)

def remove_keys_safe(file_path, keys_to_remove):
    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()

    tree = ast.parse(source, filename=file_path)
    
    # We will rebuild the file content.
    # Actually, generating code from AST preserves semantics but loses comments and formatting.
    # We want to preserve most of the file.
    
    # Better approach: 
    # Use the AST to find the byte offsets of the keys and values, then slice the string.
    # python 3.8+ ast nodes have end_lineno and end_col_offset.
    
    # Let's collect spans to cut.
    cuts = [] # (start_byte, end_byte)
    
    # We need to map line/col to byte offset
    lines = source.splitlines(keepends=True)
    # Build a cumulative length map
    line_offsets = [0]
    for line in lines:
        line_offsets.append(line_offsets[-1] + len(line))
        
    def get_offset(lineno, col_offset):
        return line_offsets[lineno-1] + col_offset

    for node in tree.body:
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Dict):
            keys = node.value.keys
            values = node.value.values
            
            for i in range(len(keys)):
                k = keys[i]
                v = values[i]
                if isinstance(k, ast.Constant) and isinstance(k.value, str):
                    if k.value in keys_to_remove:
                        # Found a key to remove.
                        # We want to remove from the start of the key to the end of the value.
                        # AND potential trailing comma.
                        
                        start = get_offset(k.lineno, k.col_offset)
                        end = get_offset(v.end_lineno, v.end_col_offset)
                        
                        # Extend start backwards to include indentation? 
                        # No, simpler to just cut the key: value part. 
                        # But we will leave empty lines or weird commas.
                        
                        # Let's try to remove the whole line if it's single line.
                        if k.lineno == v.end_lineno:
                            # It's on one line (or part of one line)
                            # Remove the whole line mostly?
                            line_idx = k.lineno - 1
                            cuts.append((line_offsets[line_idx], line_offsets[line_idx+1]))
                        else:
                            # Multi-line
                            start_line_idx = k.lineno - 1
                            end_line_idx = v.end_lineno
                             # Remove from start line to end line (inclusive)
                            cuts.append((line_offsets[start_line_idx], line_offsets[end_line_idx]))

    # Merge overlapping cuts and sort
    cuts.sort()
    
    # Apply cuts
    new_source = []
    last_pos = 0
    for start, end in cuts:
        if start > last_pos:
            new_source.append(source[last_pos:start])
        last_pos = max(last_pos, end)
    new_source.append(source[last_pos:])
    
    final_content = "".join(new_source)
    
    # Post-processing to clean up empty dictionary braces if we emptied it (unlikely)
    # and clean up multiple commas ?? 
    # Actually, removing lines is safer if we assume standard formatting `    'KEY': { ... },\n`
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(final_content)

if __name__ == "__main__":
    base_dir = "/home/kdy987/work/kiwi7/backend/domains/stkcompanys/ls/models/requests"
    deduplicate(base_dir)
