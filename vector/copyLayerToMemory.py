def copyLayerToMemory(in_lyr):
    """
    Copies a Layer to the memory, returns the copy.
    :param in_lyr: Layer of a shapefile
    :return: Copy of the layer that is stored in memory
    """

    import ogr
		
    drv_mem = ogr.GetDriverByName('Memory')
    shp_copy = drv_mem.CreateDataSource('temp')
    copy_lyr = shp_copy.CopyLayer(in_lyr, 'lyr_copy')
    in_lyr.ResetReading()
    copy_lyr.ResetReading()
    return shp_copy, copy_lyr