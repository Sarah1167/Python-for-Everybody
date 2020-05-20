fname=input('Enter a file name: ')
if fname=='1':
    fname='mbox-short.txt'
if fname=='2':
    fname='mbox.txt'
try:
    fhand=open(fname)
except:
    print('FILE NOT FOUND')
    exit()

count=0
words=[]
for line in fhand:
    if line.startswith('From '):
        count=count+1
        words=line.split()
        print(words[1])
print('There were', count, 'lines in the file with "From" as the first word')
