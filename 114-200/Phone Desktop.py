import math
opaetion=int(input())
for i in range(opaetion):
    a,b=map(int,input().split())
    if b%2==0:
        sum=a+(b*4)
    if b%2!=0:
        sum=a+(b**2)
    if sum<=15:
        if sum==0:
            print("0")
        else:
            print("1")
    elif sum%2==0:
        print(math.ceil(sum/15))
    else:
        print(math.floor(sum/15))