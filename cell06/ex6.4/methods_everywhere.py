#!/usr/bin/env python3
import sys

def shrink(s):
    # Display the first eight characters of the string
    print(s[:8])

def enlarge(s):
    # Append 'Z' to the string to make it 8 characters
    print(s.ljust(8, 'Z'))

# Check if there are command line arguments
if len(sys.argv) < 2:
    print("none")
else:
    for arg in sys.argv[1:]:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)
