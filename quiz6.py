#Claire Yegian
#12/13/17
#quiz6.py 

dictionary = open('engmix.txt')

#Program 1
list = []
for word in dictionary:
    if word.count('c') == 3 and word.count('p') == 2:
        list.append(word)
for word in list:
    word.strip()
    print(word)
    

