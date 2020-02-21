def extractGeomCharacteristics(in_shp_pth):

    """
    Extracts the area and the centroid of polygons in a layer. 
    :param in_shp_pth: Input shapefile with polygons.
    # :param id_field: Name of field with ID of polygons
    :return: Three lists, 1: List of IDs, 2: List of areas, 3: List of centroids
    """

    import ogr

    in_shp = ogr.Open(in_shp_pth, 0)
    in_lyr = in_shp.GetLayer()

    num_feat_total = in_lyr.GetFeatureCount()
    print(num_feat_total)
    id_lst = []
    area_lst = []
    centroid_lst = []
    for f, feat in enumerate(in_lyr):
        # fid = feat.GetField(id_field)
        geom = feat.GetGeometryRef()
        area = geom.Area()
        centroid = geom.Centroid()
        centroid = centroid.ExportToWkt()

        id_lst.append(f)
        area_lst.append(area)
        centroid_lst.append(centroid)

    in_lyr.ResetReading()

    return id_lst, area_lst, centroid_lst