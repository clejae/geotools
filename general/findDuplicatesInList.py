def findDuplicatesInList(lst):
    """
    Finds duplicate variables in a list.
    :param lst: Input list.
    :return: Returns duplicates of the list and the indeces of the second occurence of the duplicates (both as a list)
    """
    
    unique_set = set()
    duplicates_set = set()
    
    unique_add = unique_set.add
    duplicate_add = duplicates_set.add

    index_lst = []
    
    for i, item in enumerate(lst):
        if item in unique_set:
            duplicate_add(item)
            index_lst.append(i)
        else:
            unique_add(item)
    return list(duplicates_set), index_lst