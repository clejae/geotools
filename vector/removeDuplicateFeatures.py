def removeDuplicateFeatures(in_shp_pth, out_folder, return_duplicates=False):
	import os
	import ogr
    """
    VERY SLOW FUNCTION. 
    Loops through features of a shapefile with geom type polygon and checks for duplicates. 
    Writes a shapefile to the specified outfolder with the ending "_no_duplicates". 
    Optional: returns the duplicates as well with the ending "duplicates".
    
    ToDo:
    Get geom type from input shapefile. 
    
    :param in_shp_pth: Input shapefile.
    :param out_folder: Path to output folder. Not including the filename.
    :param return_duplicates: Boolean. Set True if duplicates should be returned.
    :return: No object returned, but shapefile written to disc. 
    """

    try:
        if not os.path.exists(out_folder):
            os.makedirs(out_folder)
    except OSError:
        print ('Error: Creating directory. ' + out_folder)

    file_name = os.path.basename(in_shp_pth)[:-4]

    in_shp = ogr.Open(in_shp_pth, 0)
    in_lyr = in_shp.GetLayer()

    copy_shp, copy_lyr = copyLayerToMemory(in_lyr)

    nodups_shp_name = out_folder + r'\\' + file_name + '_no_duplicates.shp'
    nodups_shp, nodups_lyr = createEmptyShpWithCopiedLyr(in_lyr=in_lyr, out_pth=nodups_shp_name,
                                                         geom_type=ogr.wkbPolygon)
    nodups_lyr_defn = nodups_lyr.GetLayerDefn()
    dupl_lst = []

    if return_duplicates == True:
        dups_shp_name = out_folder + r'\\' + file_name + '_duplicates.shp'
        dups_shp, dups_lyr = createEmptyShpWithCopiedLyr(in_lyr=in_lyr, out_pth=dups_shp_name,
                                                         geom_type=ogr.wkbPolygon)
        dups_lyr_defn = dups_lyr.GetLayerDefn()
        dupl_lst = []

    num_feat_total = in_lyr.GetFeatureCount()

    for f, feat_curr in enumerate(in_lyr):
        id1 = feat_curr.GetField('ID')
        geom_curr = feat_curr.GetGeometryRef()

        ## set a filter on the copied layer to identify all features that might overlap
        copy_lyr.SetSpatialFilter(geom_curr)
        num_feat_nb = copy_lyr.GetFeatureCount() -1
        progress = round((f / num_feat_total)*100, 2)
        # print("Progress:", progress, "% ID:", id1, "Neighbouring features:", num_feat_nb )
        dupl_check = 0
        for feat_nb in copy_lyr:
            id2 = feat_nb.GetField('ID')
            id_inters = '{0}_{1}'.format(min([id1, id2]), max([id1, id2]))
            geom_nb = feat_nb.geometry()

            ## if both geoms are equal and IDs differ then increase duplicate check by 1
            if geom_curr.Equals(geom_nb) and id1 != id2:
                dupl_lst.append(id_inters)
                dupl_check += 1

        ## if the current feature is not a duplicate or w
        ## if it is a duplicate but the second version of it was net yet recorded in the duplicate list
        ## then add the current feature to the no duplicates layer
        if dupl_check == 0 or dupl_lst.count(id_inters) == 1:
            ouf_feat = ogr.Feature(nodups_lyr_defn)
            for i in range(0, nodups_lyr_defn.GetFieldCount()):
                field_def = nodups_lyr_defn.GetFieldDefn(i)
                field_name = field_def.GetName()
                ouf_feat.SetField(field_name, feat_curr.GetField(i))
            geom_out = geom_curr.Clone()
            geom_out = geom_out.MakeValid()
            ouf_feat.SetGeometry(geom_out)
            nodups_lyr.CreateFeature(ouf_feat)
            ouf_feat = None
        else:
            if return_duplicates == True:
                ouf_feat = ogr.Feature(dups_lyr_defn)
                for i in range(0, dups_lyr_defn.GetFieldCount()):
                    field_def = dups_lyr_defn.GetFieldDefn(i)
                    field_name = field_def.GetName()
                    ouf_feat.SetField(field_name, feat_curr.GetField(i))
                geom_out = geom_curr.Clone()
                geom_out = geom_out.MakeValid()
                ouf_feat.SetGeometry(geom_out)
                dups_lyr.CreateFeature(ouf_feat)
                ouf_feat = None
            else:
                pass

        copy_lyr.SetSpatialFilter(None)
        copy_lyr.ResetReading()
    in_lyr.ResetReading()
    nodups_lyr.ResetReading()

    del copy_shp, copy_lyr
    del nodups_shp, nodups_lyr
    del in_shp, in_lyr
    if return_duplicates == True:
        del dups_lyr, dups_shp