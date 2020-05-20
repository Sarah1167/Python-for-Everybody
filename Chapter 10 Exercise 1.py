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

email_addresses={}

for line in fhand:
    if line.startswith('From '):
        email=line.split()[1]
        email_addresses[email]=email_addresses.get(email, 0)+1

max_value=0
max_address=None
for key in email_addresses:
    if email_addresses[key] > max_value:
        max_value=email_addresses[key]
        max_address=key

print(max_address, max_value)
