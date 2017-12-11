dictionary = open('engmix.txt')

"""word2 = input('Enter a word: ')
x = ''
for word in dictionary:
    word = word.strip()
    if word==word2:
        x = word
if x!='':
    print('Your word is in the dictionary')
else:
    print('Your word is not in the dictionary')"""


"""wordList = []
for word in dictionary:
    wordList.append(word)

num = int(input('Enter a number: '))
print(wordList[num-1])"""


fileName = input('Enter a file name: ')

file = open(fileName)

fileLines = []
for line in file:
    fileLines.append(line.strip())

fileLines.reverse()
for item in fileLines:
    print(item+'!')


"""letter = input('Enter a letter: ')
greatestLetter = ''
greatestNumber = 0
for word in dictionary:
    if letter in word:
        if word.count(letter)>greatestNumber:
            greatestLetter = word
            greatestNumber = word.count(letter)
print(greatestLetter)"""
