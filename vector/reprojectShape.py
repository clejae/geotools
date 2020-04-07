def reprojectShape(in_shp, out_shp_pth, out_sr_epsg, geom_type):
    """
    Function found at: https://pcjericks.github.io/py-gdalogr-cookbook/projection.html. Slightly changed.

    Reprojects a shapefile to given spatial reference.

    :param in_shp: Input shapefile .
    :param out_shp_pth: Output path to which the reprojected shapefile will be written.
                        Should include filename.
    :param out_sr_epsg: EPSG number of target spatial reference.
    :param geom_type: Geometry type of output shapefile.
    :return: No object returned, but shapefile will be written to disc.
    """

    from osgeo import ogr, osr
    import os

    drv = ogr.GetDriverByName('ESRI Shapefile')

    # get the input layer
    in_lyr = in_shp.GetLayer()

    # input SpatialReference
    in_sr = in_lyr.GetSpatialRef()

    # output SpatialReference
    out_sr = osr.SpatialReference()
    out_sr.ImportFromEPSG(out_sr_epsg)

    # create the CoordinateTransformation
    coord_trans = osr.CoordinateTransformation(in_sr, out_sr)

    # create the output layer
    if os.path.exists(out_shp_pth):
        drv.DeleteDataSource(out_shp_pth)
    out_shp = drv.CreateDataSource(out_shp_pth)
    lyr_name = os.path.splitext(os.path.split(out_shp_pth)[1])[0]
    out_lyr = out_shp.CreateLayer(lyr_name, geom_type=geom_type)

    # add fields
    in_lyr_defn = in_lyr.GetLayerDefn()
    for i in range(0, in_lyr_defn.GetFieldCount()):
        field_defn = in_lyr_defn.GetFieldDefn(i)
        out_lyr.CreateField(field_defn)

    # get the output layer's feature definition
    out_lyr_defn = out_lyr.GetLayerDefn()

    # loop through the input features
    for in_feat in in_lyr:
        # get the input geometry
        geom = in_feat.GetGeometryRef()
        # reproject the geometry
        geom.Transform(coord_trans)
        # create a new feature
        out_feat = ogr.Feature(out_lyr_defn)
        # set the geometry and attribute
        out_feat.SetGeometry(geom)
        for i in range(0, out_lyr_defn.GetFieldCount()):
            out_feat.SetField(out_lyr_defn.GetFieldDefn(i).GetNameRef(), in_feat.GetField(i))
        # add the feature to the shapefile
        out_lyr.CreateFeature(out_feat)
        # dereference the features and get the next input feature
        out_feat = None
    in_lyr.ResetReading()

    # Save and close the shapefiles
    in_shp = None
    out_shp = None