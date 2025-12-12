line=int(input())
for i in range(line):
    a=input()
    l1=a[0]
    l2=a[1]
    l3=a[2]
    l4=a[3]
    l5=a[4]
    l6=a[5]
    l1=int(l1)
    l2=int(l2)
    l3=int(l3)
    l4=int(l4)
    l5=int(l5)
    l6=int(l6)
    x=l1+l2+l3
    y=l4+l5+l6
    if x != y:
        print("NO")
    else :
        print("YES")