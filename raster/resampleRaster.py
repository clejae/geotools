def resampleRaster(src_filename, extent, res, dst_filename, resampling_method, dst_proj=None, driver='GTiff'):
    x_min = extent[0]
    x_max = extent[1]
    y_min = extent[2]
    y_max = extent[3]
    width = math.ceil((x_max - x_min) / res)
    height = math.ceil((y_max - y_min) / res)

    gt = (x_min, res, 0.0, y_max, 0.0, -res)

    ## Open source file, get metadata
    src = gdal.Open(src_filename, gdalconst.GA_ReadOnly)
    src_proj = src.GetProjection()
    src_geotrans = src.GetGeoTransform()
    src_bands = src.RasterCount

    # Output / destination
    dst = gdal.GetDriverByName(driver).Create(dst_filename, width, height, src_bands, gdalconst.GDT_Float32)
    dst.SetGeoTransform(gt)
    if dst_proj:
        proj = dst_proj
    else:
        proj = src_proj
    dst.SetProjection(proj)

    # Do the work
    gdal.ReprojectImage(src, dst, src_proj, proj, resampling_method)
