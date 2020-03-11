def identifyEntailedFeatures(in_shp_pth,  id_field="ID", margin = 0):
    """

    :param in_shp_pth:
    :param id_field:
    :return:
    """
    import vector
    import ogr

    in_shp = ogr.Open(in_shp_pth, 0)
    in_lyr = in_shp.GetLayer()

    copy_shp, copy_lyr = vector.copyLayerToMemory(in_lyr)

    out_lst = []

    for feat_curr in in_lyr:

        id1 = feat_curr.GetField(id_field)
        # print("FEATURE: {}".format(id1))
        geom_curr = feat_curr.GetGeometryRef()
        geom_curr = geom_curr.Buffer(margin)

        copy_lyr.SetSpatialFilter(geom_curr)

        for feat_nb in copy_lyr:
            id2 = feat_nb.GetField(id_field)
            geom_nb = feat_nb.GetGeometryRef()

            if id1 != id2:
                if geom_nb.Within(geom_curr):

                    out_lst.append(id2)

        copy_lyr.ResetReading()
    in_lyr.ResetReading()

    return(out_lst)

    ## SLOW VERSION
    # import ogr
    #
    # in_shp = ogr.Open(in_shp_pth, 0)
    # in_lyr = in_shp.GetLayer()
    #
    # num_feat = in_lyr.GetFeatureCount()
    #
    # out_lst = []
    #
    # for n in range(num_feat):
    #     feat_curr = in_lyr.GetFeature(n)
    #     fid = feat_curr.GetField(id_field)
    #     # print("FEATURE: {}".format(fid))
    #
    #     geom_curr = feat_curr.GetGeometryRef()
    #     geom_curr = geom_curr.Buffer(margin)
    #
    #     in_lyr.SetSpatialFilter(geom_curr)
    #
    #     for feat_nb in in_lyr:
    #         fid_nb = feat_nb.GetField(id_field)
    #         geom_nb = feat_nb.GetGeometryRef()
    #         if fid != fid_nb:
    #             if geom_nb.Within(geom_curr):
    #                 out_lst.append(fid_nb)
    #     in_lyr.ResetReading()
    #
    # return (out_lst)