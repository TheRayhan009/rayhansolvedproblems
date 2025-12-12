oparetion=int(input())
for i in range(oparetion):
    a,b,c=map(int,input().split())
    x=[]
    x.append(a)
    x.append(b)
    x.append(c)
    x.sort()
    # x=x[1]
    y=abs(int(x[1])-int(x[0]))
    z=abs(int(x[1])-int(x[2]))
    print(y+z)