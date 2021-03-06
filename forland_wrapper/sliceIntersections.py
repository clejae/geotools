def sliceIntersections(in_shp_pth, final_out_shp):

    """
    This function looks for intersections of intersections (thus the intersections need to be calculated beforehand
    via the function vector.identifyIntersections). It does this in a loop until no further intersections can be
    identified. Finally, it creates an output file, where all intersections are broken down to several polygons.
    These polygons carry the field "IDInters" which tells the user which original polygons are overlapping at these
    small intersection polygons.
    :param in_shp_pth: Path to input shapefile, including file name. String.
    :param final_out_shp: Path to output shapefile, including file name. String.
    :return: Writes the output file to the disc.
    """

    import os
    import ogr
    import vector
    import forland_wrapper

    QgsApplication, QgsProcessingRegistry, start_app, QgsNativeAlgorithms, processing, app = vector.importQgis()
    QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())

    in_shp = ogr.Open(in_shp_pth)
    in_lyr = in_shp.GetLayer()

    num_feat = in_lyr.GetFeatureCount()

    drv = ogr.GetDriverByName("ESRI Shapefile")

    ## Identify intersections, as long as there were intersections detected
    in_pth_temp = in_shp_pth
    i = 0
    while num_feat > 0:
        # print(i)
        i += 1
        out_shp_pth = in_shp_pth[:-4] + '_{0:02d}.shp'.format(i)
        print(out_shp_pth)
        vector.identifyIntersectionsSec(in_pth_temp, out_shp_pth, id_field='IDInters')

        out_shp = ogr.Open(out_shp_pth)
        out_lyr = out_shp.GetLayer()
        num_feat = out_lyr.GetFeatureCount()
        in_pth_temp = out_shp_pth

        del out_shp, out_lyr

    ## delete the file, that was lasty created and
    ## that has effectively no geoms (i.e. intersections) in it
    if i > 0:
        drv.DeleteDataSource(out_shp_pth)
        # os.remove(out_shp_pth)
        # os.remove(out_shp_pth[:-3] + 'dbf')
        # os.remove(out_shp_pth[:-3] + 'prj')
        # os.remove(out_shp_pth[:-3] + 'shx')

    ## remove the intersections from the upper-level layer
    ## and afterwards add the intersection geoms to the upper level layer
    ## --> all intersections areas are sliced
    i = i - 1
    if i == 1:
        input_shp = in_shp_pth
        overlay_shp = in_shp_pth[:-4] + '_01.shp'
        output_shp = in_shp_pth[:-4] + '_difference.shp'
        forland_wrapper.validityChecking(overlay_shp)
        param_dict = {'INPUT': input_shp, 'OVERLAY': overlay_shp, 'OUTPUT': output_shp}
        print(param_dict)
        processing.run('native:difference', param_dict)

        merge_layers = [output_shp, overlay_shp]
        param_dict = {'LAYERS': merge_layers, 'CRS': merge_layers[0], 'OUTPUT': final_out_shp}
        processing.run('qgis:mergevectorlayers', param_dict)
    elif i > 1:
        merge_layers = [in_shp_pth[:-4] + '_{0:02d}.shp'.format(i)]
        for x in range(i, 1, -1):
            input_shp = in_shp_pth[:-4] + '_{0:02d}.shp'.format(x-1)
            forland_wrapper.validityChecking(input_shp)
            overlay_shp = in_shp_pth[:-4] + '_{0:02d}.shp'.format(x)
            forland_wrapper.validityChecking(overlay_shp)
            output_shp = in_shp_pth[:-4] + '_{0:02d}_difference.shp'.format(x-1,x)
            param_dict = {'INPUT': input_shp, 'OVERLAY': overlay_shp, 'OUTPUT': output_shp}
            print(param_dict)
            processing.run('native:difference', param_dict)

            merge_layers.append(output_shp)
        input_shp = in_shp_pth
        overlay_shp = in_shp_pth[:-4] + '_01.shp'
        output_shp = in_shp_pth[:-4] + '_difference.shp'
        param_dict = {'INPUT': input_shp, 'OVERLAY': overlay_shp, 'OUTPUT': output_shp}
        print(param_dict)
        processing.run('native:difference', param_dict)

        merge_layers.append(output_shp)
        print(merge_layers)

        param_dict = {'LAYERS': merge_layers, 'CRS': merge_layers[0], 'OUTPUT': final_out_shp}
        processing.run('qgis:mergevectorlayers', param_dict)

    else:
        print("The input shapefile does not have any intersections.")