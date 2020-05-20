#Write a program that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the values are.
fname=input('Enter a txt File name, that you want to enter all the words into a Python Dictionary: ')
if fname=='1':
    fname='words.txt'
try:
    fhand=open(fname, 'r')
except:
    print('FILE NOT FOUND')

dwords={}
for line in fhand:
    word = line.split()
    for c in word:
        dwords[c] = dwords.get(c,0)#+1

print(dwords)
