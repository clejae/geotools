def makeGeomsValid(in_shp_pth, id_field_name ="ID"):
    """
    Makes geoms valid by buffering it with 0 and appliyng the .MakeValid()-ogr function.
    :param in_shp_pth: Input Shapefile
    :return: Updates the input shapefile.
    """

    import ogr

    in_shp = ogr.Open(in_shp_pth, 1)
    in_lyr = in_shp.GetLayer()
    for feat in in_lyr:
        geom = feat.GetGeometryRef()
        fid = feat.GetField(id_field_name)
        # print(fid)
        if not geom.IsValid() and geom != 'NoneType':

            # print(in_shp_pth, ':', fid)
            # print("Geom_in is valid:", geom.IsValid())

            geom_out = geom.MakeValid()
            geom_out.Buffer(0)
            # print(geom_out.GetGeometryName())
            # print("Geom_out is valid:", geom_out.IsValid())
            # assert feature.GetGeometryRef().IsValid()

            feat.SetGeometry(geom_out.Buffer(0))
            # feat.SetGeometryDirectly(geom_out)

            in_lyr.SetFeature(feat)

        else:
            pass

    in_lyr.ResetReading()

    del in_shp, in_lyr