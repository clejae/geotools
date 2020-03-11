def orderAndConcatItems(in_str):
    """
    Very specific function: it turns a string containing
    multiple numbers concatenated by '_' into a list of numbers e.g. 1_4_6_2_1 --> [1, 4, 6, 2, 1]
    Then it orders the list and removes duplicates --> 1, 2, 4, 6
    Finally, the remaining ordered numbers are concatenated again with '_' --> 1_2_4_6
    :param str: A string containing multiple numbers concatenated by '_'.
    :return: Ordered string
    """
    str_split = in_str.split('_')
    str_split = [int(float(id)) for id in str_split]
    str_split.sort()
    str_split = list(set(str_split))
    str_split = [str(id) for id in str_split]
    out_str = '_'.join(str_split)

    return out_str