def deleteShp(pth):
    """
    Deletes a shapefile and all its associated files.
    :param pth: Path to a shapefile
    """
    import ogr
    import os

    driver = ogr.GetDriverByName("ESRI Shapefile")
    if os.path.exists(pth):
        driver.DeleteDataSource(pth)