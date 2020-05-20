words=[]
fhand=open('romeo.txt')
for lines in fhand:
    for word in lines.split():
#OK youTube cowboy did it this way, but this isn't taught until Chapter 9!!!!!!!        
        if word not in words:
            words.append(word)
print(sorted(words))
