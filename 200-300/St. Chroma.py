n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    l=[]
    if y>=x:
        for j in range(y):
            l.append(str(j))
        print(" ".join(l))
    else:
        for j in range(y):
            l.append(str(j))
        for j in range(y+1,x):
            l.append(str(j))
        if x!=1:
            l.append(str(y))
        if x==1 and y==0:
            l.append(str(y))
        print(" ".join(l))
        