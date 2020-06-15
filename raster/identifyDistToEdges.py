def identifyDistToEdges(arr, i = 3):
    """
    Calculates the distance inside clusters to their edges. Problem:

    :param arr: Input array. Integer with values of 0 and 1.
    :param i: Number of cells that the distance will be calculated inwards.
    :return: Array with distances to edges in cell numbers as a unit. The inner parts will have i+1 assigned.
    """
    ## calc distance to edge
    out_arr = arr * (i + 1)
    calc_arr = arr.copy()
    for i in range(1,i+1):

        ## calculate edges
        sx = ndimage.sobel(calc_arr, axis=0, mode='constant')
        sy = ndimage.sobel(calc_arr, axis=1, mode='constant')
        arr_comb = np.hypot(sx, sy)
        arr_edges = np.logical_and(calc_arr > 0, arr_comb > 0)

        ## save to out_arr
        arr_edges = arr_edges * i
        out_arr = np.where(arr_edges > 0, arr_edges, out_arr)

        ## buffer inwards
        calc_arr = 1 - calc_arr
        kernel = np.ones((3,3))
        arr_buff = np.int64(convolve2d(calc_arr, kernel, mode = 'same') > 0)
        arr_buff = 1 - arr_buff
        calc_arr = arr_buff.copy()

    return out_arr