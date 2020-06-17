def exploreShp(shp, num_feat):
    """
    Prints the attributes of all fields for the specified number of features in the layer of the input shapefile.
    :param shp: Input shapefile
    :num_feat: Number of features for which the attributes will be printed.
    """
    import vector

    lyr = shp.GetLayer()
    fnames = vector.getFieldNames(shp)
    print(fnames)
    for i in range(num_feat):
        feat = lyr.GetFeature(i)
        print_lst = []
        for fname in fnames:
            attr = feat.GetField(fname)
            print_lst.append(attr)
        print(print_lst)
    lyr.ResetReading()
