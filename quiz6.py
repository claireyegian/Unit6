#Claire Yegian
#12/13/17
#quiz6.py 

dictionary = open('engmix.txt')

#Program 1
3c = []
2p = []
for word in dictionary:
    if word.count('c') == 3:
        3c.append(word)
    if word.count('p') == p:
        2p.append(word)
print(3c,'all have 3 cs')
print(2p,'all have 2 ps')
    

