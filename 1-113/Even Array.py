oparations=int(input())
for i in range(oparations):
    l=int(input())
    even=0
    odd=0
    eliments=list(map(int,input().split()))
    for j in range(l):
        if j%2==0:
            if eliments[j]%2!=0:
                odd=odd+1
        elif j%2 != 0:
            if eliments[j]%2==0:
                even=even+1
    if even==odd:
        print(even)
    else:
        print("-1")
