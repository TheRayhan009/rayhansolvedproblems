import math
oparetion=int(input())
for i in range(oparetion):
    a,b,c,x,y=map(int,input().split())
    tota_food=a+b+c
    total_animals=x+y
    if a<x:
        a_need=abs(x-a)
        c=c-a_need
    if b<y:
        b_need=abs(b-y)
        c=c-b_need
    if a>=x and b>=y:
        print("YES")
    elif c>=0:
        print("YES")
    else:
        print("NO")