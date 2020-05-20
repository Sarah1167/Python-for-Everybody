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
email=[]
emaillist=[]
for line in fhand:
    if line.startswith('From '):
        count=count+1
        words=line.split()
        email=words[1]
        if email not in emaillist:
            emaillist.append(email)
emaillist.sort()
print('\n'.join(emaillist))

print('\nThere were', count, 'lines in the file with "From" as the first word')
