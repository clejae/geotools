def openRasterFromList(raster_pth_lst):
    """
    Opens all rasters from the provided list and puts them in an output list.
    :param raster_pth_lst: List of raster paths which should be opened.
    :return: List of opened rasters.
    """

    import gdal
    rasterList = []
    for rastername in raster_pth_lst:
        raster = gdal.Open(rastername)
        rasterList.append(raster)

    return rasterList
