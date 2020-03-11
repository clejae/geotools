def removingNoneGeoms(in_shp_pth, out_shp_pth, id_field = "ID"):
    """
    This function checks if there are features with no geometry and deletes them.
    :param in_shp_pth: Path to input shapefile. String.
    :param out_shp_pth: Path to output shapefile, including filename. String.
    :param id_field: ID field, for function countNoneGeoms. String. Default = "ID".
    :return:
    """


    import vector

    print("Removing features with no geometry in:", in_shp_pth)
    none_geomes = vector.countNoneGeoms(in_shp_pth, id_field)
    if len (none_geomes) > 0:
        # out_shp_pth = in_shp_pth[:-4] + '_cleaned.shp'
        vector.removeNoneGeoms(in_shp_pth, out_shp_pth)
        print("All features with no geometry removed. New SHP:", out_shp_pth)
    else:
        pass