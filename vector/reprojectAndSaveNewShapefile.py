def reprojectAndSaveNewShapefile(inFilepath,outFilepath,to_EPSG):
    """
    Reprojects a given Shapefile into a specified Coordinate system.
    :param inFilepath: Full path with file name of input Shapefile, string
    :param ouFilepath: Full path with file name of output Shapefile, string
    :param to_EPSG: EPSG that defines the Coordinate System, Integer
    :return:
    """
    import geopandas as gpd
    from fiona.crs import from_epsg

    inFile = gpd.read_file(inFilepath)
    inFile_proj = inFile.copy()
    inFile_proj['geometry'] = inFile_proj['geometry'].to_crs(epsg=to_EPSG)
    inFile_proj.crs = from_epsg(to_EPSG)
    inFile_proj.to_file(outFilepath)
