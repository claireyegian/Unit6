#Claire Yegian
#12/6/17
#zzwords.py - prints all words in dictionary that contain 'zz'

dictionary = open('engmix.txt')

for word in dictionary:
    if 'zz' in word:
        print(word.strip())
