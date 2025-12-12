oparetions=int(input())
for i in range(oparetions):
    num=int(input())
    # chaka=0
    chakb=0
    index=0
    for j in range(num):
        a,b=map(int,input().split())
        if a<=10:
            if chakb<b:
                chakb=b
                index=j
    print(index+1)
    