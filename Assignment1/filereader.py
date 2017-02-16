def parseMatrixFile(matrixFile):
    matrixContents = []
    with open(matrixFile,"r") as m:
        fileContent = m.readlines()
    fileContent = fileContent[3:]
    fileContent = [line.strip() for line in fileContent]

    for line in fileContent:
        if(line == 'A' or line == 'B' or line == 'C'):
            matrixContents.append(fileContent[fileContent.index(line):fileContent.index(line) + 4])
        elif(line == '1' or line == '2' or line == '3' or line == '4' or line == '5' or line == '6'):
            matrixContents.append(fileContent[fileContent.index(line):fileContent.index(line) + 4])
    return matrixContents    
