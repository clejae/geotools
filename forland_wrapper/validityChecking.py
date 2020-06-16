def validityChecking(in_shp_pth, id_field_name ="ID"):
    import vector

    print("Validity check of", in_shp_pth)
    invalid_geoms = vector.countInvalidGeoms(in_shp_pth = in_shp_pth, id_field_name = id_field_name)
    if len(invalid_geoms) > 0:
        vector.makeGeomsValid(in_shp_pth = in_shp_pth, id_field_name= id_field_name)
        invalid_geoms_step2 = vector.countInvalidGeoms(in_shp_pth = in_shp_pth, id_field_name = id_field_name)

        if len(invalid_geoms_step2) > 0:
            print(invalid_geoms_step2, "could not be made valid.")
            file = open(in_shp_pth[:-3] + 'txt', "w+")
            file.write(str(invalid_geoms_step2) + " could not be made valid.")
            file.close()
        else:
            print("All invalid geometries were made valid.")
    else:
        print("There are no invalid geometries in shapefile", in_shp_pth)