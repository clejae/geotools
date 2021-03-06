def getCorners(path):
    """
    Extracts the corners of a raster
	:param path: Path to raster including filename.
	:return: Minimum X, Minimum Y, Maximum X, Maximum Y
    """
    import gdal
    ds = gdal.Open(path)
    gt = ds.GetGeoTransform()
    width = ds.RasterXSize
    height = ds.RasterYSize
    minx = gt[0]
    miny = gt[3] + width * gt[4] + height * gt[5]
    maxx = gt[0] + width * gt[1] + height * gt[2]
    maxy = gt[3]
    return minx, miny, maxx, maxy

