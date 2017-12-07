#Claire Yegian
#12/6/17
#howManyWords.py - prints number of words for each number of letters

dictionary = open('engmix.txt')

letters = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for word in dictionary:
    letters[len(word)-1] = (letters[len(word)-1] + 1)

w = 0
for item in letters:
    print('There are',letters[w],w,'letter words')
    w += 1
