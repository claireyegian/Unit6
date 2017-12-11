#Claire Yegian
#12/7/17
#longShort.py - prints shortest and longest words for each letter of alphabet

dictionary = open('engmix.txt')

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

dictionaryList = []
for word in dictionary:
    word = word.strip()
    if word != '':
        dictionaryList.append(word)
dictionaryList.sort

longest =['']*26
shortest = ['']*26
alphabetNum = 0
for line in dictionaryList:
    letter = alphabet[alphabetNum]
    letterList = []
    while line[0] == letter:
        letterList.append(line)
    longestWord = 0
    longestword = ''
    for item in letterList:
        if len(item)>=longestWord:
            longestWord = len(item)
            longestword = item
        longest[alphabetNum] = longestword
    shortestWord = longestWord
    shortestword = ''
    for wordd in letterList:
        if len(wordd)<=shortestWord:
            shortestWord = len(wordd)
            shortestword = wordd
        shortest[alphabetNum] = wordd
    alphabetNum = alphabetNum + 1