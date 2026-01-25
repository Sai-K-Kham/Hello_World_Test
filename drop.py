fileOne = open('file1.txt','r')
fileTwo = open('file2.txt','w')
for line in fileOne:
    fileTwo.write(line)
fileOne.close()
fileTwo.close()
