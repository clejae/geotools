def reprojectAndSaveNewRaster(inFilepath,outFilepath,to_EPSG):
    """
    Reprojects a given raster to the specified Coordinate System
    :param inFilepath: Full path of input file including filename and extension, string
    :param outFilepath: Full path of output file including filename and extension, string
    :param to_EPSG: EPSG number, integer
    :return:
    """
    from osgeo import gdal
    input_raster = gdal.Open(inFilepath)
    EPSG_string = "EPSG:"+str(to_EPSG)
    ras = gdal.Warp(outFilepath,input_raster,dstSRS=EPSG_string)
    del ras
