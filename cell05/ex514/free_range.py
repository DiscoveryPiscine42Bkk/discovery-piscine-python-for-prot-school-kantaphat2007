#!/usr/bin/env python3
import sys

# Check if there are exactly two parameters
if len(sys.argv) != 3:
    print("none")
else:
    # Convert the parameters to integers
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    
    # Create a list using range
    result = list(range(start, end + 1))
    
    # Print the list
    print(result)
