def stackMultibandRasters(ras_lst, out_path):
	'''

	Creates a stack of rasters with the same x and y dimensions.
	The datatype of the output raster is based on the datatype of the first raster in the list.

	:param ras_lst: List of raster objects. Rasters must have the same x and y dimensions.
	:param out_path: Full path and name of output file.
	:return: A Geotiff raster.
	'''
	import gdal
	n = len(ras_lst)
	bands = ras_lst[0].RasterCount
	x_res = ras_lst[0].RasterXSize
	y_res = ras_lst[0].RasterYSize

	nbands_out = 0
	for ras in ras_lst:
		num_bands = ras.RasterCount
		nbands_out = nbands_out + num_bands

	# nbands_out  = n * bands

	data_type = ras_lst[0].GetRasterBand(1).DataType
	# data_type = gdal.GetDataTypeName(data_type)

	no_data_value = ras_lst[0].GetRasterBand(1).GetNoDataValue()
	gt = ras_lst[0].GetGeoTransform()
	pr = ras_lst[0].GetProjection()

	print(
		'Create raster stack with {0} bands, {1} columns and {2} rows of datatype {3}.'.format(nbands_out, x_res, y_res,
																							   data_type))

	out_ras = gdal.GetDriverByName('GTiff').Create(out_path, x_res, y_res, nbands_out, data_type)
	out_ras.SetGeoTransform(gt)
	out_ras.SetProjection(pr)

	# Iterate over all rasters in the input list. For each raster, loop over the bands.

	curr_i = 0
	for r, ras in enumerate(ras_lst):
		print('Band {0}/{1}'.format(r + 1, n))
		for b in range(1, bands + 1):
			curr_i += 1
			# print(curr_i)

			# Get the current band and its array.
			curr_band = ras.GetRasterBand(b)
			curr_arr = curr_band.ReadAsArray()

			# Create an index for the output raster. Get band i of output raster. Write the array to band i.

			out_band = out_ras.GetRasterBand(curr_i)
			out_band.WriteArray(curr_arr)
			out_band.SetNoDataValue(no_data_value)
			out_band.FlushCache()
		print('done')

	del (out_ras)