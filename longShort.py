#Claire Yegian
#12/7/17
#longShort.py - prints shortest and longest words for each letter of alphabet

dictionary = open('engmix.txt')

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

longest =['']*26
shortest = ['']*26
alphabetNum = 0
for word in dictionary:
    word = word.strip()
    if word != '':
        letter = alphabet[alphabetNum]
        letterList = []
        while word[0] == letter:
            letterList.append(word)
            longestWord.letter = 0
            longestword.letter = ''
            for line in letterList:
                if len(line)>=longestWord.letter:
                    longestWord.letter = len(line)
                    longestword.letter = word
            longest[alphabetNum] = longestword.letter
            shortestWord.letter = longestWord.letter
            shortestword.letter = ''
            for line in letterList:
                if len(line)<=