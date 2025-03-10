#!/usr/bin/env python3
import sys

# Check if there are no parameters passed
if len(sys.argv) == 1:
    print("none")
else:
    # Print the number of parameters
    print(f"parameters: {len(sys.argv) - 1}")

    # Loop through each parameter and print the parameter and its length
    for param in sys.argv[1:]:
        print(f"{param}: {len(param)}")
