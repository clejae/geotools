def stackRasterFromList(rasterList, outputPath):
    """
    Stacks the first band of n rasters that are stored in a list. The properties
    of the first raster are used to set the definition of the output raster.
    rasterList - list containing the rasters that have the same dimensions and Spatial References
    outputPath - Path including the name to which the stack is written
    """
    import gdal

    gt = rasterList[0].GetGeoTransform()
    pr = rasterList[0].GetProjection()
    data_type = rasterList[0].GetRasterBand(1).DataType
    x_res = rasterList[0].RasterXSize
    y_res = rasterList[0].RasterYSize

    target_ds = gdal.GetDriverByName('GTiff').Create(outputPath, x_res, y_res, len(rasterList), data_type)
    target_ds.SetGeoTransform(gt)
    target_ds.SetProjection(pr)

    for i in range(0, len(rasterList)):
        band = target_ds.GetRasterBand(i + 1)
        no_data_value = rasterList[i].GetRasterBand(1).GetNoDataValue()
        band.WriteArray(rasterList[i].GetRasterBand(1).ReadAsArray())
        band.SetNoDataValue(no_data_value)
        band.FlushCache()

    del(target_ds)