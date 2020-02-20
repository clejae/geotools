def writeListToCSV(inputList, outputFile):
    """
    Write a provided list with several sublists(i.e. the rows) into a csv File. Every sublist is written into one line.
    :param inputList: List that contains several sublists. List[Sublist,Sublist,etc]
    :param outputFile: Name of output File with ending .csv. String
    :return: Returns provided list as csv file.
    """
    outputFile = open(outputFile, 'w')
    for subList in inputList:
        i = 0
        for subitem in subList:
            if i < len(inputList[0]) - 1:
                outputFile.write(str(subitem))
                outputFile.write(",")
                i += 1
            else:
                outputFile.write(str(subitem))
        outputFile.write('\n')
    del outputFile
