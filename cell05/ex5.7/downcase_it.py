#!/usr/bin/env python3
import sys

# Check if exactly one parameter is passed
if len(sys.argv) == 2:
    # Print the string in lowercase
    print(sys.argv[1].lower())
else:
    # Print "none" if the number of parameters is different from 1
    print("none")
