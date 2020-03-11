def removeLooseLines(in_shp_pth, out_shp_pth, dissolve=False , dist = -.01):

    import vector
    import os
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

