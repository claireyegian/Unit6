#Claire Yegian
#12/7/17
#reverseFile.py - asks for name of file and prints all lines of file in reverse

fileName = input('Enter a file name: ')

file = open(fileName)

fileLines = []
for line in file:
    fileLines.append(line)

fileLines.reverse()
print(fileLines)
