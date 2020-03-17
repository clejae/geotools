def writeArrayToRaster(in_array, out_path, gt, pr, no_data_value, type_code=None, options=['COMPRESS=DEFLATE']):
    """
    Writes an array to a tiff-raster. If no type code of output is given, it will be extracted from the input array.
    As default a deflate compression is used, but can be specified by the user.
    :param in_array: Input array
    :param out_path: Path of output raster
    :param gt: GeoTransfrom of output raster
    :param pr: Projection of output raster
    :param no_data_value: Value that should be recognized as the no data value
    :return: Writes an array to a raster file on the disc.
    """

    import gdal
    from osgeo import gdal_array

    if type_code == None:
        type_code = gdal_array.NumericTypeCodeToGDALTypeCode(in_array.dtype)

    if len(in_array.shape) == 3:
        nbands_out = in_array.shape[0]
        x_res = in_array.shape[2]
        y_res = in_array.shape[1]

        out_ras = gdal.GetDriverByName('GTiff').Create(out_path, x_res, y_res, nbands_out, type_code, options=options)
        out_ras.SetGeoTransform(gt)
        out_ras.SetProjection(pr)

        for b in range(0, nbands_out):
            band = out_ras.GetRasterBand(b + 1)
            arr_out = in_array[b, :, :]
            band.WriteArray(arr_out)
            band.SetNoDataValue(no_data_value)
            band.FlushCache()

        del (out_ras)

    if len(in_array.shape) == 2:
        nbands_out = 1
        x_res = in_array.shape[1]
        y_res = in_array.shape[0]

        out_ras = gdal.GetDriverByName('GTiff').Create(out_path, x_res, y_res, nbands_out, type_code, options=options)
        out_ras.SetGeoTransform(gt)
        out_ras.SetProjection(pr)

        band = out_ras.GetRasterBand(1)
        band.WriteArray(in_array)
        band.SetNoDataValue(no_data_value)
        band.FlushCache()

        del (out_ras)