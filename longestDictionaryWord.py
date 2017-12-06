#Claire Yegian
#12/6/17
#longestDictionaryWord.py - longest word in dictionary

dictionary = open('engmix.txt')

longestWord = 0
longestword = ''
for word in dictionary:
    if len(word)>=longestWord:
        longestWord = len(word)
        longestword = word

print(longestword)