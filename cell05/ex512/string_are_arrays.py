#!/usr/bin/env python3
import sys

# Check if there is exactly one parameter passed
if len(sys.argv) != 2:
    print("none")
else:
    # Get the string from the parameter
    input_string = sys.argv[1]
    
    # Find all occurrences of the character 'z' (case-sensitive)
    z_count = input_string.count('z')
    
    # If there are no 'z' characters, print "none"
    if z_count == 0:
        print("none")
    else:
        # Print 'z' for each occurrence of 'z'
        print('z' * z_count)
