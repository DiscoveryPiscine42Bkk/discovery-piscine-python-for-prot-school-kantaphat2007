#!/usr/bin/env python3
import sys

# Check if no parameters are passed
if len(sys.argv) == 1:
    print("none")
else:
    # Iterate over the parameters, skipping those that already end with "ism"
    for param in sys.argv[1:]:
        if not param.endswith("ism"):
            print(param + "ism")
