import math
lines=int(input())
l=list(map(int,input().split()))
for i in range(lines):
    x=math.sqrt(l[i])
    if l[i]==1:
        print("NO")
    elif x%1==0:
        print("YES")
    else:
        print("NO")