def validitiyCheck(in_shp_pth, id_field_name):
    """
    Checks the validity of geoms in a shapefile. 
    :param in_shp_pth: Input shapefile
    :param id_field_name: Field name of ID, string.
    :return: Returns a list of IDs of the features that are not valid.
    """
    import ogr

    in_shp = ogr.Open(in_shp_pth)
    in_lyr = in_shp.GetLayer()

    out_lst = []

    for feat in in_lyr:
        geom = feat.GetGeometryRef()
        fid = feat.GetField(id_field_name)
        if geom.IsValid():
            pass
        else:
            out_lst.append(fid)

    in_lyr.ResetReading()

    del in_shp, in_lyr

    return(out_lst)