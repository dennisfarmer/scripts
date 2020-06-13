#!/usr/bin/env python

import pickle
import sys
import json

nested_json = False

with open(sys.argv[1], "rb") as f:
    pickle_data = pickle.load(f)

try:
    if isinstance(pickle_data[0], dict):
        nested_json = True
        print(json.dumps(pickle_data, indent=2))
except:
    pass

if not nested_json:
    if isinstance(pickle_data, dict):
        print(json.dumps(pickle_data, indent=2))
    else:
        print(pickle_data)
