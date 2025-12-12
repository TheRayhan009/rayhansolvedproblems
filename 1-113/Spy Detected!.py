lines=int(input())
for i in range(lines):
    z=int(input())
    input1=list(map(int,input().split()))
    maxes=max(input1)
    minex=min(input1)
    x=0
    y=0
    for j in range(len(input1)):
        if input1[j]==maxes:
            x=x+1
        else:
            y=y+1
    if x<y:
        print(input1.index(maxes)+1)
    else:
        print(input1.index(minex)+1)