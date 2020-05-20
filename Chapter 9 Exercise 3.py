fname=input('Enter file name: ')
if fname=='1':
    fname='mbox-short.txt'
try:
    fhand=open(fname, 'r')
except:
    print('FILE NOT FOUND')
    exit()

email={}

for line in fhand:
    if not line.startswith('From '):
        continue
    line=line.rstrip()
    words=line.split()
    em=words[1]
    if em not in email:
        email[em]=1
    else:
        email[em]+=1

print(email)
