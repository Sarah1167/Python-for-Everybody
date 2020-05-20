def chop(list):
    fchop=list[1:]
    onumb=len(fchop)
    none=fchop[:onumb-1]
    print(none)
    return none

def middle(mlist):
    newmlist=mlist[1:]
    nnumb=len(newmlist)
    new=newmlist[:nnumb-1]
    print(new)
    return new

fruit=['peach', 'plumb', 'orange', 'pineapple', 'mango']
print(fruit)

x=chop(fruit)
y=middle(fruit)

if x==y:
    print('Shits identical AND equivalent yo!')
else:
    print('Damn, it\'s equivalent but NOT identical.')
