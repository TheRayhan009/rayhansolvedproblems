import math
opa=int(input())
for i in range(opa):
    n=int(input())
    if n%2!=0:
        print("0")
    else:
        x=n/2
        x=math.floor(x/2)+1
        print(x)