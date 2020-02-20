def getDateList(ras):
    """
    Extracts a list of all dates that are saved in the output of a FORCE time series. Dates must be stored in Metainfo 
    of the raster data set.
    :param ras: Input raster file (e.g. NDVI time series)
    :return: List of all dates.
    """
    
    import gdal
    import re

    options = gdal.InfoOptions(allMetadata=True)
    info = gdal.Info(ras, options=options)
    out_lst = re.findall('Date=(.*)T', info)
    
    return out_lst