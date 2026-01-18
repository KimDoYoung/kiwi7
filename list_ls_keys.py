
import os
import sys

# Add the project root to sys.path
sys.path.append(os.getcwd())

from backend.domains.ls.models.ls_response_definition import LS_RESPONSE_DEF

keys = sorted(LS_RESPONSE_DEF.keys())
print(f"Total keys: {len(keys)}")
for key in keys:
    print(key)
