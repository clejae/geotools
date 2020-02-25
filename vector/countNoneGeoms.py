def countNoneGeoms(in_shp_pth, id_field_name):
    """
    Counts the occurence of features that have no geometries.

    :param in_shp_pth: Input shapefile
    :param id_field_name: Field name of ID, string.
    :return: Returns a list of IDs of the features that have no geometries.
    """

    import ogr

    in_shp = ogr.Open(in_shp_pth, 1)
    in_lyr = in_shp.GetLayer()

    out_lst = []

    for feat in in_lyr:
        geom = feat.GetGeometryRef()
        fid = feat.GetField("ID")

        if geom == None:
            out_lst.append(fid)
        else:
            pass

    del in_shp, in_lyr
    print("The input shapefile has {} feature(s) that has/have no geometry.".format(len(out_lst)))
    return (out_lst)