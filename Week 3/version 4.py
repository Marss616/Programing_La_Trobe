def determine_book_language(isbn):
    """
    Determines the language of a book based on its ISBN.

    Args:
    isbn (int): The ISBN of the book.

    Returns:
    str: The language of the book.
    """

    # Convert 13-digit ISBN starting with 978 to 10-digit ISBN
    if 9780000000000 <= isbn <= 9789999999999:
        isbn -= 9780000000000

    # Determine the language based on the ISBN
    if 0 <= isbn <= 1999999999:
        return "English"
    elif 2000000000 <= isbn <= 2999999999:
        return "French"
    elif 3000000000 <= isbn <= 3999999999:
        return "German"
    else:
        return "Unknown"

# Example usage
example_isbn = 9781581820089
language = determine_book_language(example_isbn)

print(determine_book_language(1000001001))
