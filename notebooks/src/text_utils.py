"""Utilities for cleaning and formatting text."""


def clean_name(raw):
    """Remove extra whitespace and convert a name to title case."""
    return " ".join(raw.split()).title()
