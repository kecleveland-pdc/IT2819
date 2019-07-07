with open("A08input.txt", "r+") as txtFile:
    outputFile = open("A08output.txt", "w+")
    for txtLine in txtFile:
        print(txtLine)
        outputFile.write(txtLine)
    outputFile.close()    
txtFile.close()