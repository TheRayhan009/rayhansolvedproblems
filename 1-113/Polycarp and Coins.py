oparations=int(input())
for i in range(oparations):
    line=int(input())
    x=line
    c1=int(line/3)
    c2=int(line/3)
    if line%3==1:
        c1=c1+1
    elif line%3==2:
        c2=c2+1
    print(c1,c2)
