def importQgis():
    ## QGIS
    from qgis.core import QgsApplication, QgsProcessingRegistry
    from qgis.testing import start_app
    from qgis.analysis import QgsNativeAlgorithms
    import processing
    app = start_app()
    QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())

    return QgsApplication, QgsProcessingRegistry, start_app,  QgsNativeAlgorithms, processing, app

