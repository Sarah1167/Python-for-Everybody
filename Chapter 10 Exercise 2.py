# look through the dictionary using a maximum loop to ﬁnd who has the most messages
#print how many messages the person has.
fname=input('Enter file name: ')
if fname=='1':
    fname='mbox-short.txt'
if fname=='2':
    fname='mbox.txt'
try:
    fhand=open(fname, 'r')
except:
    print('FILE NOT FOUND')
    exit()

email_hour={}
#pulling and counting the "hour"
for line in fhand:
    if line.startswith('From '):
        time=line.split()[5]
        hour=time.split(':')[0]
        email_hour[hour]=email_hour.get(hour, 0)+1

lst = list()
for key, val in list(email_hour.items()):
    lst.append((key, val))

lst.sort()

for key, val in lst:
    print(key, val)
