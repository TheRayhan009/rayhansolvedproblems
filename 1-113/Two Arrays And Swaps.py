oparations=int(input())
for i in range(oparations):
    indexx,sowip=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ans=0
    preans=0
    for l in range(len(a)):
        preans=preans+a[l]
    for j in range(sowip):
        x=min(a)
        x=a.index(x)
        y=max(b)
        c=a[x]
        #n=b.index(y)
        if c<=y:
            a[x]=y
            b.remove(y)
        else:
            break
    for k in range(len(a)):
        ans=ans+int(a[k])
    if preans<ans:
        print(ans)
    else:
        print(preans)

