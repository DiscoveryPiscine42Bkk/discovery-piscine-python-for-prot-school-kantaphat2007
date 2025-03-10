def find_the_redheads(family_dict):
    """
    This function filters out family members with red hair.
    :param family_dict: Dictionary with names as keys and hair colors as values.
    :return: List of names with red hair.
    """
    return list(filter(lambda name: family_dict[name] == "red", family_dict))

# Example usage
dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))
