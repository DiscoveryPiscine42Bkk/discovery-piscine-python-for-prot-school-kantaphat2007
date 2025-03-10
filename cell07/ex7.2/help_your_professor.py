def average(class_scores):
    """
    This function calculates the average score of a class.
    :param class_scores: Dictionary with student names as keys and their scores as values.
    :return: The average score of the class.
    """
    return sum(class_scores.values()) / len(class_scores) if class_scores else 0

# Example usage
class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}

class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")
