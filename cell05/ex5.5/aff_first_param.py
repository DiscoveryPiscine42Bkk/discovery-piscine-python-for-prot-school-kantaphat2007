#!/usr/bin/env python3
import sys

# Check if there are parameters passed
if len(sys.argv) > 1:
    # Print the first parameter
    print(sys.argv[1])
else:
    # Print "none" if no parameters are passed
    print("none")