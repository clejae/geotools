def printFieldNames(lyr):
    """
    Prints the field names and type, width and precision of field.
    :param lyr: Input layer of a shapefile
    :return: Print.
    """
    
    lyr_defn = lyr.GetLayerDefn()
    print("Column name | Field type | Width | Precision")
    print("--------------------------------------------")
    for i in range(lyr_defn.GetFieldCount()):
        field_name = lyr_defn.GetFieldDefn(i).GetName()
        field_type_code = lyr_defn.GetFieldDefn(i).GetType()
        field_type = lyr_defn.GetFieldDefn(i).GetFieldTypeName(field_type_code)
        field_width = lyr_defn.GetFieldDefn(i).GetWidth()
        get_precision = lyr_defn.GetFieldDefn(i).GetPrecision()

        print(field_name + " | " + field_type + " | " + str(field_width) + " | " + str(get_precision))