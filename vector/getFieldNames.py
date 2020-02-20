def getFieldNames(shp):
    """
    :param shp: Shapefile to get the field names from
    :return: List of all field names
    """
	
	import ogr
	
    lyr = shp.GetLayer()
    lyr_def = lyr.GetLayerDefn()

    fname_lst = []
    for i in range(lyr_def.GetFieldCount()):
        fname = lyr_def.GetFieldDefn(i).GetName()
        fname_lst.append(fname)

    return fname_lst