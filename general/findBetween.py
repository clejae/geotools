def findBetween(str, first, last):
    """
    Finds a string between two specified substrings.
    :param str: Input string, string.
    :param first: First substring, string.
    :param last: Second substring, string.
    :return: Returns the string between the two substrings.
    """
    
    try:
        start = str.index(first) + len(first)
        end = str.index(last, start)
        return str[start:end]
    except ValueError:
        return ""