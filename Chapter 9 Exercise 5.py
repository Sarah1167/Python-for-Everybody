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

email_domain={}
for line in fhand:
    if line.startswith('From '):
        email=line.split()[1]
        atpos= email.find('@')
        stoppos=email.find(' ', atpos)
        host=email[atpos+1:stoppos]
        email_domain[host]=email_domain.get(host, 0)+1

print(email_domain)
