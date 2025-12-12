lines=int(input())
for i in range(lines):
    element=int(input())
    a=list(map(int,input().split()))
    a.sort()
    chak=a[0]
    x=0
    for j in range(len(a)):
        if a[0]==chak or a[0]==chak+1:
            chak=a[0]
            a.remove(a[0])
        else:
            x=1
            print("NO")
            break
    if x==0:
        print("YES")