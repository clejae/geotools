def createEmptyShpWithCopiedLyr(in_lyr, out_pth, geom_type):
    import ogr
    """
    Creates a shapefile (at an user defined path)
    that has the same fields as the input shapefile
    and that has an user defined geometry type
    :param in_lyr: Input layer from which the layer definition is copied
    :param out_pth: Path were copy is stored.
    :param geom_type: Geometry type of the output shapefile, e.g. ogr.wkbPolygon or ogr.wkbMultiPolygon
    :return: Output shapefile, output Layer
    """
    drv_shp = ogr.GetDriverByName('ESRI Shapefile')
    in_sr = in_lyr.GetSpatialRef()
    in_lyr_defn = in_lyr.GetLayerDefn()
    if os.path.exists(out_pth):
        drv_shp.DeleteDataSource(out_pth)
    shp_out = drv_shp.CreateDataSource(out_pth)
    lyr_name = os.path.splitext(os.path.split(out_pth)[1])[0]
    lyr_out = shp_out.CreateLayer(lyr_name, in_sr, geom_type=geom_type)
    for i in range(0, in_lyr_defn.GetFieldCount()):
            field_def = in_lyr_defn.GetFieldDefn(i)
            lyr_out.CreateField(field_def)
    return shp_out, lyr_out