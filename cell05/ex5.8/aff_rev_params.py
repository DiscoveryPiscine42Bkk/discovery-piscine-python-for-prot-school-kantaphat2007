#!/usr/bin/env python3
import sys

# Check if there are fewer than two parameters
if len(sys.argv) < 2:
    print("none")
else:
    # Print the parameters in reverse order
    for param in reversed(sys.argv[1:]):
        print(param)
