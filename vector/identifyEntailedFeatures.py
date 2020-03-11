def removeEntailedFeatures(in_shp_pth,  id_field="ID", margin = 0):
    """

    :param in_shp_pth:
    :param id_field:
    :return:
    """
    import os
    import ogr
    import vector

    in_shp = ogr.Open(in_shp_pth, 0)
    in_lyr = in_shp.GetLayer()

    copy_shp, copy_lyr = vector.copyLayerToMemory(in_lyr)

    out_lst = []

    for feat_curr in in_lyr:

        id1 = feat_curr.GetField(id_field)
        print("FEATURE: {}".format(id1))
        geom_curr = feat_curr.GetGeometryRef()
        area_curr = geom_curr.Area()
        copy_lyr.SetSpatialFilter(geom_curr)


        for feat_nb in copy_lyr:
            id2 = feat_nb.GetField(id_field)
            geom_nb = feat_nb.GetGeometryRef()
            area_nb = geom_nb.Area()
            if id1 != id2:
                # if geom_nb.Within(geom_curr):
                # if geom_curr.Within(geom_nb):
                #     out_lst.append(id2)
                #     print("Feature {} is within feature {}".format(id2, id1))
                intersection = geom_nb.Intersection(geom_curr)
                geom_type = intersection.GetGeometryName()
                if geom_type not in ['POLYGON',
                                     'MULTIPOLYGON']:  # in ['MULTILINESTRING', 'POINT', 'LINESTRING','MULTIPOINT']: #alternatively
                    intersection = None
                    area_inters = 0
                    # print("Intersection of {} and {} is a {}".format(id1, id2, geom_type))
                elif intersection != None:
                    area_inters = intersection.Area()
                    # print("Intersection of {} and {} is NOT none. Its area is {} and its geom type is {}".format(id1, id2, area_inters, geom_type))
                else:
                    intersection = None
                    area_inters = 0

                print("Area 1: {} \n Area 2: {} \n Area I: {}".format(area_curr, area_nb, area_inters))

                if round(area_inters,0)  == round(area_nb,0):
                    out_lst.append(id2)
                    print("Feature {} is within feature {}".format(id2, id1))


        copy_lyr.ResetReading()
    in_lyr.ResetReading()

    return(out_lst)