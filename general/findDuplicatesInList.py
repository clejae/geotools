def findDuplicatesInList(lst):
    """
    Finds duplicate variables in a list.
    :param lst: Input list.
    :return: Returns duplicates of the list as a list.
    """
    
    unique = set()
    duplicates = set()
    
    unique_add = unique.add
    duplicate_add = duplicates.add
    
    for item in enumerate(lst):
        if item in unique:
            duplicate_add(item)
        else:
            unique_add(item)
    return list(duplicates)
