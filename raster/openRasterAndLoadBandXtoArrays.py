def openRastersAndLoadBandXtoArrays(rasternameList,bn):
    """Full Paths need to be provided.
    bn - bandnumber"""
    import gdal
    rasterList = []
    arrayList =[]
    for rastername in rasternameList:
        ds = (gdal.Open(rastername))
        rasterList.append(ds)
        cols = ds.RasterXSize
        rows = ds.RasterYSize
        arrayList.append(np.array(ds.GetRasterBand(bn).ReadAsArray(0,0,cols,rows)))
    return rasterList, arrayList
