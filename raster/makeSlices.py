def makeSlices(array, win_size):
    """
    Returns a list of slices given a window size.
    :param array: Two-dimensional array to get slices from.
    :param win_size: tuple of (rows, columns) for the moving window
    :return: Slices
    """
    rows = array.shape[0] - win_size[0] + 1
    cols = array.shape[1] - win_size[1] + 1
    slices = []
    for i in range(win_size[0]):
        for j in range(win_size[1]):
            slices.append(array[i:rows + i, j:cols + j])
    return slices

