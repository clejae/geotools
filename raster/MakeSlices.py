def MakeSlices(array, win_size):
    """Return a list of slices given a window size.
    data     - two-dimensional array to get slices from
    win_size - tuple of (rows, columns) for the moving window
    """
    rows = array.shape[0] - win_size[0] + 1
    cols = array.shape[1] - win_size[1] + 1
    slices = []
    for i in range(win_size[0]):
        for j in range(win_size[1]):
            slices.append(array[i:rows + i, j:cols + j])
    return slices

