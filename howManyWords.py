#Claire Yegian
#12/6/17
#howManyWords.py - prints number of words for each number of letters

dictionary = open('engmix.txt')

letters = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

i = 1
for word in dictionary:
    if len(word) == i:
        letters[i-1] = (letters[i-1] + 1)
    i += 1

w = 0
for item in letters:
    print('There are',letters[w],letters[w],'letter words')
    w += 1
