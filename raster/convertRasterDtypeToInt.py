def convertRasterDtypeToInt(in_path, out_path, scale_factor = 1):
    '''
    This function converts the datatype of an input raster to integer, if possible. Provide a scale_factor greater than
    1 if the values need to be increased. This should be done, when there are decimal places that should not be lost.
    If the raster is not scaled and there are decimal places, then they will be lost because during the conversion,
    there will be a rounding. Only signed integer datatypes will be assigned. Depending on the maximum value the right
    integer data type will be chosen (max <= 127 --> int8, max <= 32767 --> int16, max <= 2147483647 --> int32).
    If the maximum value is above 2147483647 then float 64 will be assigned.

    :param in_path: Path and filename to input raster.
    :param out_path: Path and filename to output raster.
    :param scale_factor: Scale factor which will be used to scale the input raster. Default: 1.
    :return: Raster file at location of out_path.
    '''

    import gdal
    import numpy as np
    from osgeo import gdal_array

    in_ras = gdal.Open(in_path)

    gt = in_ras.GetGeoTransform()
    pr = in_ras.GetProjection()
    no_data_value = in_ras.GetRasterBand(1).GetNoDataValue()

    in_array = in_ras.ReadAsArray()

    in_array = in_array * scale_factor
    in_array = in_array.astype(int)

    if np.max(in_array) <= 127:
        type_code = 1
    if np.max(in_array) > 127 and np.max(in_array) < 32767:
        type_code = 3
    elif np.max(in_array) > 32767 and np.max(in_array) < 2147483647:
        type_code = 5
    if np.max(in_array) > 214748364:
        print("Cannot use integer datatype, using instead float64.")
        type_code = 7

    if len(in_array.shape) == 3:
        nbands_out = in_array.shape[0]
        x_res = in_array.shape[2]
        y_res = in_array.shape[1]

        out_ras = gdal.GetDriverByName('GTiff').Create(out_path, x_res, y_res, nbands_out, type_code)
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

        out_ras = gdal.GetDriverByName('GTiff').Create(out_path, x_res, y_res, nbands_out, type_code)
        out_ras.SetGeoTransform(gt)
        out_ras.SetProjection(pr)

        band = out_ras.GetRasterBand( 1)
        band.WriteArray(in_array)
        band.SetNoDataValue(no_data_value)
        band.FlushCache()

        del (out_ras)