def removingNoneGeoms(in_shp_pth, out_shp_pth, id_field = "ID"):
    print("Removing features with no geometry in:", in_shp_pth)
    none_geomes = vector.countNoneGeoms(in_shp_pth, id_field)
    if len (none_geomes) > 0:
        # out_shp_pth = in_shp_pth[:-4] + '_cleaned.shp'
        vector.removeNoneGeoms(in_shp_pth, out_shp_pth)
        print("All features with no geometry removed. New SHP:", out_shp_pth)
    else:
        pass