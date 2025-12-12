clookstring=input()
c=clookstring.upper()
x=clookstring[0].lower()
y=clookstring[1:len(clookstring)+1].upper()
if clookstring[0]==x and clookstring[1:len(clookstring)+1]==y:
    x=x.upper()
    y=clookstring[1:len(clookstring)+1].lower()
    print(x,end=""+y)

elif c==clookstring:
    c=clookstring.lower()
    print(c)

else:
    for i in range(len(clookstring)):
        if x==clookstring[0].lower() and clookstring[i]==clookstring[i].lower():
            print(clookstring)
            break