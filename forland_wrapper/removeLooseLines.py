def removeLooseLines(in_shp_pth, out_shp_pth, dissolve=False , dist = -.01):

    """
    This function removes either loose lines outside or inside of polygons.
    If dist is negative then outside loose lines will be removed, if it is positive,
    then loose lines inside of polygons will be removed.
    :param in_shp_pth: Path to input shapefile. String.
    :param out_shp_pth: Path to output shapefile, incl. filename. String.
    :param dissolve: Wether polygons should be dissolved. Boolean. Default = False.
    :param dist: Buffering parameter. Real. Default -0.01.
    :return:
    """

    import vector

    QgsApplication, QgsProcessingRegistry, start_app, QgsNativeAlgorithms, processing, app = vector.importQgis()
    QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())

    buff_pth = out_shp_pth[:-4] + '_buff.shp'
    processing.run("native:buffer", {'INPUT': in_shp_pth,
                                     'DISTANCE': dist,
                                     'SEGMENTS': 5,
                                     'DISSOLVE': dissolve,
                                     'END_CAP_STYLE': 2,
                                     'JOIN_STYLE': 2,
                                     'MITER_LIMIT': 2,
                                     'OUTPUT': buff_pth})

    processing.run("native:buffer", {'INPUT': buff_pth,
                                     'DISTANCE': -dist,
                                     'SEGMENTS': 5,
                                     'DISSOLVE': dissolve,
                                     'END_CAP_STYLE': 2,
                                     'JOIN_STYLE': 1,
                                     'MITER_LIMIT': 2,
                                     'OUTPUT': out_shp_pth})

