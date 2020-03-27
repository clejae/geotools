def cloneFieldDefn(src_def):

    fdef = ogr.FieldDefn(src_def.GetName(), src_def.GetType())
    fdef.SetWidth(src_def.GetWidth())
    fdef.SetPrecision(src_def.GetPrecision())

    return fdef