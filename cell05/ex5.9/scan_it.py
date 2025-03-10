#!/usr/bin/env python3
import sys

# Check if there are exactly two parameters
if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    string_to_search = sys.argv[2]
    
    # Count how many times the keyword appears in the string
    count = string_to_search.count(keyword)
    
    # If the keyword doesn't appear, print "none"
    if count == 0:
        print("none")
    else:
        print(count)
