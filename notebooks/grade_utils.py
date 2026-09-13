"""Utility module for converting numeric GPAs to letter grades on a 5.00 scale."""


def letter_grade(gpa):
    """Return the letter grade corresponding to a numeric GPA."""
    if gpa >= 4.50:
        return "A"
    elif gpa >= 3.50:
        return "B"
    elif gpa >= 2.50:
        return "C"
    elif gpa >= 1.50:
        return "D"
    else:
        return "F"
