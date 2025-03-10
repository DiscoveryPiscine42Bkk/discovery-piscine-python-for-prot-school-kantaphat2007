#!/usr/bin/env python3

def array_of_names(names_dict):
    return [f"{first.capitalize()} {last.capitalize()}" for first, last in names_dict.items()]

# Define the dictionary of names
persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

# Print the result of calling array_of_names
print(array_of_names(persons))
