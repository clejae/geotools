def writeListToCSV(in_lst, out_pth, sep = ","):
    """
    Writes a provided list with several sub lists (which will represent the rows) into a csv File.
    Every sub list is written into one line.
    :param in_lst: List that contains several sub lists: List[Sublist,Sublist,etc]
    :param out_pth: Path, including name of output file with ending .csv. String
    :param sep: Optional, specify a separator, default: comma. String
    :return: Returns provided list as csv file.
    """
    out_file = open(out_pth, 'w')
    for sub_lst in in_lst:
        length = len(sub_lst)

        for i in range(length-1):
            item = sub_lst[i]
            out_file.write(str(item))
            out_file.write(sep)

        item = sub_lst[length-1]
        out_file.write(str(item))
        out_file.write('\n')

    del out_file

    #     for item in sub_lst:
    #         if i < len(inputList[0]) - 1:
    #             outputFile.write(str(item))
    #             outputFile.write(",")
    #             i += 1
    #         else:
    #             outputFile.write(str(item))
    #     outputFile.write('\n')
    # del outputFile
