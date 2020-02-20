def openRastersAndLoadBandXtoArrays(raster_pth_lst, bn):
    """
    Loads all rasters to a list and all bands at index bn of these rasters to another list. 
    :param raster_pth_lst: List of raster paths from which the bands should be extracted.
    :param bn: Band number which should be loaded.
    :return: List of rasters and list of arrays of the specified bands
    """
    """Full Paths need to be provided.
    bn - bandnumber"""
    import gdal
    rasterList = []
    arrayList =[]
    for rastername in raster_pth_lst:
        ds = (gdal.Open(rastername))
        rasterList.append(ds)
        cols = ds.RasterXSize
        rows = ds.RasterYSize
        arrayList.append(np.array(ds.GetRasterBand(bn).ReadAsArray(0,0,cols,rows)))
    return rasterList, arrayList
