def SpatialReferenceFromRaster(raster):
    """
    Returns SpatialReference from raster dataset
    :param raster: Input raster dataset
    :return: Spatial Reference
    """
    ''''''
    import osr
    pr = raster.GetProjection()
    sr = osr.SpatialReference()
    sr.ImportFromWkt(pr)
    return sr