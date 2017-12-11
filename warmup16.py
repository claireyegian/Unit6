#Claire Yegian
#12/11/17
#warmup16.py - all words that start with 'c' and end with 'y'

dictionary = open('engmix.txt')

for word in dictionary:
    if word.strip()[0] == 'c':
        if word.strip()[-1] == 'y':
            print(word)
