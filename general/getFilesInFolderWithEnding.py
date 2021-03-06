def getFilesinFolderWithEnding(folder, ext, fullPath):
    """
    Opens all files with the specified extention in a specified folder.
    :param folder: Folder in which the files should be searched, string.
    :param ext: Data file extention that should be searched (e.g. txt), string.
    :param fullPath: Boolean
    :return:
    """
    """
    """
    import os
    outlist = []
    input_list = os.listdir(folder)
    if fullPath == True:
        for file in input_list:
            if file.endswith(ext):
                if folder.endswith("/"):
                    filepath = folder + file
                else:
                    filepath = folder + "/" + file
                outlist.append(filepath)
    if fullPath == False or fullPath == None:
        for file in input_list:
            if file.endswith(ext):
                outlist.append(file)
    if len(outlist) == 1:
        print("Found only one file matching the extension. Returning a variable instead of a list")
        outlist = outlist[0]
    if len(outlist) == 0:
        print("Could not find any file matching the extension. Return-value is None")
    return outlist

