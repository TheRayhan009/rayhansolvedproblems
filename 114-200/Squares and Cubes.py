oparetion=int(input())
for i in range(oparetion):
    num=int(input())
    root=0
    ans=0
    a=False
    b=False
    for j in range(0,num):
        root=j*j
        cube=j*j*j
        if root>=num:
            a=True
        if cube>=num:
            b=True
        if a==True and b==True:
            break
        if root<=num:
            ans+=1
        if cube<=num:
            ans+=1
    print(ans)