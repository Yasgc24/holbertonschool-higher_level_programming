#!/usr/bin/python3
"""7. Load, add, save"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    item = load_from_json_file("add_item.json")
except Exception:
    item = []
for a in range(1, len(sys.argv)):
    item.append(sys.argv[a])
save_to_json_file(item, "add_item.json")
