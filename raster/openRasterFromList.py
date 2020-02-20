def openRasterFromList(rasternameList):
    import gdal
    rasterList = []
    for rastername in rasternameList:
        raster = gdal.Open(rastername)
        rasterList.append(raster)
    return rasterList
