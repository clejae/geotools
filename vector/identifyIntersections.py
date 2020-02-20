def identifyIntersections(in_shp_pth, out_pth):
    """
    VERY SLOW
    Identifies intersections between polygons of a shapefile. Writes intersections specfied output path.
    :param in_shp_pth: Input shapefile of polygons.
    :param out_pth: Output path to which the intersections are written. Input filename will be extended by
    "_intersection".
    :return: No object returned, but shapefile will be written to disc.
    """
	
	import os
	import ogr

    file_name = os.path.basename(in_shp_pth)[:-4]

    try:
        if not os.path.exists(out_pth):
            os.makedirs(out_pth)
    except OSError:
        print('Error: Creating directory. ' + out_pth)

    in_shp = ogr.Open(in_shp_pth, 0)
    in_lyr = in_shp.GetLayer()

    copy_shp, copy_lyr = copyLayerToMemory(in_lyr)

    inters_shp_name = out_pth + r'\\' + file_name + '_intersection.shp'
    drv_shp = ogr.GetDriverByName('ESRI Shapefile')
    in_sr = in_lyr.GetSpatialRef()
    if os.path.exists(inters_shp_name):
        drv_shp.DeleteDataSource(inters_shp_name)
    inters_shp = drv_shp.CreateDataSource(inters_shp_name)
    lyr_name = os.path.splitext(os.path.split(inters_shp_name)[1])[0]
    geom_type = ogr.wkbPolygon
    inters_lyr = inters_shp.CreateLayer(lyr_name, in_sr, geom_type=geom_type)
    inters_lyr.CreateField(ogr.FieldDefn('ID', ogr.OFTInteger64))
    inters_lyr.CreateField(ogr.FieldDefn('IDInters', ogr.OFTString))

    inters_lyr_defn = inters_lyr.GetLayerDefn()
    num_fields = inters_lyr_defn.GetFieldCount()

    id_inters_lst = []
    for feat_curr in in_lyr:
        id1 = feat_curr.GetField('ID')
        geom_curr = feat_curr.GetGeometryRef()
        copy_lyr.SetSpatialFilter(geom_curr)

        for feat_nb in copy_lyr:
            id2 = feat_nb.GetField('ID')
            id_inters = '{0}_{1}'.format(min([id1, id2]), max([id1, id2]))
            geom_nb = feat_nb.geometry()
            if id1 != id2:
                if geom_nb.Intersects(geom_curr):
                    intersection = geom_nb.Intersection(geom_curr)
                    geom_type = intersection.GetGeometryName()
                    if geom_type in ['MULTILINESTRING', 'POINT', 'LINESTRING','MULTIPOINT']: #alternatively mabye not in ['POLYGON', 'MULTIPOLYGON']
                        intersection = None
                        area_inters = 0
                        # print("Intersection of {} and {} is a {}".format(id1, id2, geom_type))
                    elif intersection != None:
                        area_inters = round(intersection.Area(), 1)
                        print("Intersection of {} and {} is NOT none. Its area is {} and its geom type is {}".format(id1, id2, area_inters, geom_type))
                    else:
                        intersection = None
                        area_inters = 0
                        # print("Intersection of {} and {} is none. Its area is {}".format(id1, id2, area_inters))
                else:
                    intersection = None
                    area_inters = 0
                    # print("{} and {} do not intersect.")

                ## if the id of the intersection is not already in the list and its area is bigger than 0
                ## then add this feature to the intersection layer
                if area_inters > 0.0 and id_inters not in id_inters_lst:
                    intersection = intersection.Buffer(0)
                    intersection = intersection.MakeValid()
                    wkt_inters = intersection.ExportToWkt()
                    poly = ogr.CreateGeometryFromWkt(wkt_inters)
                    out_feat = ogr.Feature(inters_lyr_defn)
                    out_feat.SetGeometry(poly)
                    out_feat.SetField('ID', id1)
                    out_feat.SetField(num_fields - 1, id_inters)
                    inters_lyr.CreateFeature(out_feat)
                    ouf_feat = None

                    id_inters_lst.append(id_inters)
            else:
                pass

        copy_lyr.SetSpatialFilter(None)
        copy_lyr.ResetReading()
    in_lyr.ResetReading()
    inters_lyr.ResetReading()

    del copy_shp, copy_lyr
    del inters_shp, inters_lyr
    del in_shp, in_lyr