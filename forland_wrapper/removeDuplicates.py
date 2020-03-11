def removeDuplicates(in_shp_pth, no_dups_pth):

    """
    This function looks for duplicates of feautres based on two geometry criteria (area and centroid).
    If the same area and centroid occur in another geometry as well,
    only the first feature will be written to the output shapefile.
    :param in_shp_pth: Path to input shapefile. String.
    :param no_dups_pth: Path to output shapefile, including file name and ".shp". String.
    :return: Output shapefile will be written to specified location.
    """

    import general
    import vector
    import ogr

    id_lst, area_lst, centroid_lst = vector.extractGeomCharacteristics(in_shp_pth)

    ## look for identical areas and centroids
    ## the area and centroid indices indicate the occurence of possible duplicates (only the second occurence)
    area_duplicates, area_indices = general.findDuplicatesInList(area_lst)
    centroid_duplicates, centroid_indices = general.findDuplicatesInList(centroid_lst)

    ## check for indices that indicate duplicates in areas and centroids
    identical_indices = []
    for index in area_indices:
        if index in centroid_indices:
            identical_indices.append(index)

    ## remove all second occurences from the total ID list
    id_rem_lst = [id_lst[item] for item in identical_indices]
    id_unique_lst = [item for item in id_lst if item not in id_rem_lst]

    ## write the features that are indicated by the cleaned ID list to a new shapefile
    print("1.1 Writing cleaned shapefile")
    in_shp = ogr.Open(in_shp_pth, 0)
    in_lyr = in_shp.GetLayer()

    out_shp, out_lyr = vector.createEmptyShpWithCopiedLyr(in_lyr=in_lyr, out_pth=no_dups_pth, geom_type=ogr.wkbPolygon)

    if len(id_unique_lst) > 0:
        for id in id_unique_lst:
            feat = in_lyr.GetFeature(id)
            out_lyr.CreateFeature(feat)
        del out_shp, out_lyr
    else:
        print("There are not duplicates in", in_shp_pth)