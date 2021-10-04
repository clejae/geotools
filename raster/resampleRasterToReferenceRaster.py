def resample_raster_to_reference_raster(src_filename, match_filename, dst_filename, resampling_method, driver='GTiff'):
    from osgeo import gdal
    from osgeo import gdalconst

    src = gdal.Open(src_filename, gdalconst.GA_ReadOnly)
    src_proj = src.GetProjection()
    src_bands = src.RasterCount

    # We want a section of source that matches this:
    match_ds = gdal.Open(match_filename, gdalconst.GA_ReadOnly)
    match_proj = match_ds.GetProjection()
    match_geotrans = match_ds.GetGeoTransform()
    wide = match_ds.RasterXSize
    high = match_ds.RasterYSize

    # Output / destination
    dst = gdal.GetDriverByName(driver).Create(dst_filename, wide, high, src_bands, gdalconst.GDT_Float32)
    dst.SetGeoTransform(match_geotrans)
    dst.SetProjection(match_proj)

    # Do the work
    gdal.ReprojectImage(src, dst, src_proj, match_proj, resampling_method)

    del(dst)
