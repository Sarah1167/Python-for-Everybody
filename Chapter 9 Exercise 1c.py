fname=input('Enter file name: ')
if fname=='1':
    fname='romeo.txt'
try:
    fhand=open(fname, 'r')
except:
    print('FILE NOT FOUND')
    exit()
d={}
for line in fhand:
    words = line.split()
    for word in words:
        d[word] = d.get(word,0)+1
        print(word, d[word])
#This ship gets the wors out of the text file, prints the each own line with a count of how many times used so far.
print(d)
