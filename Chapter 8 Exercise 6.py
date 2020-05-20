numb=None
numblist=list()
print('When finished entering numbers type "done"')
while numb!='done':
    try:
        numb=input('Enter numbers for Max/Min processing: ')
    except:
        print('Please enter a numeric value only')

    if numb!="done":
        numb=float(numb)
        numblist.append(numb)

print('Maximum:', max(numblist))
print('Minimum:', min(numblist))
