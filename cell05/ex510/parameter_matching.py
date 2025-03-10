#!/usr/bin/env python3

import sys

# Check if exactly one parameter is passed
if len(sys.argv) != 2:
    print("none")
else:
    # Prompt the user to enter a word
    user_input = input("What was the parameter? ")

    # Compare the input with the parameter passed
    if user_input == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")
