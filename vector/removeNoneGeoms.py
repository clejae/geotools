def removeNoneGeoms(in_shp_pth, out_shp_pth):

    """
    Sometimes a shapefile has features, that have no geoms. This function removes any geom that is None.

    ToDo:
    - Use feat to write new shapefile instead of creating it from the geometries, see makeValid()

    :param in_shp_pth: Input shapefile  
    :return: Updates the input shapefile.
    """

    import vector
    import ogr

    in_shp = ogr.Open(in_shp_pth, 0)
    in_lyr = in_shp.GetLayer()

    nonones_shp, nonones_lyr = vector.createEmptyShpWithCopiedLyr(in_lyr=in_lyr, out_pth=out_shp_pth,
                                                         geom_type=ogr.wkbPolygon)
    nonones_lyr_defn = nonones_lyr.GetLayerDefn()

    for f, feat in enumerate(in_lyr):

        geom = feat.GetGeometryRef()

        if not geom == None:
            nonones_lyr.CreateFeature(feat)
            # ouf_feat = ogr.Feature(nonones_lyr_defn)
            # for i in range(0, nonones_lyr_defn.GetFieldCount()):
            #     field_def = nonones_lyr_defn.GetFieldDefn(i)
            #     field_name = field_def.GetName()
            #     ouf_feat.SetField(field_name, feat.GetField(i))
            # ouf_feat.SetGeometry(geom)
            # nonones_lyr.CreateFeature(ouf_feat)
            # ouf_feat = None
            # print(geom)
        else:
            pass
    in_lyr.ResetReading()

    del in_shp, in_lyr
    del nonones_shp, nonones_lyr