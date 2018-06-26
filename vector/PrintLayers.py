def PrintLayers(path):
    """Prints all available layer in a folder."""
    import ogr
    ds = ogr.Open(path, 0)
    if ds is None:
        raise OSError('Could not open {}'.format(fn))
    for i in range(ds.GetLayerCount()):
        lyr = ds.GetLayer(i)
        print('{0}: {1}'.format(i, lyr.GetName()))
