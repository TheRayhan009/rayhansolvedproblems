oparetion=int(input())
for i in range(oparetion):
    n=int(input())
    x=0
    for j in range(len(str(n))):
        n=str(n)
        if n[-1]==0:
            x+=1
        else:
            break
    print(len(n)-x)