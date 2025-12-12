import math
oparetions=int(input())
for i in range(oparetions):
    b_a,b_b,b_c=map(int,input().split())
    b_c_cil=math.ceil(b_c/2)
    b_c_floor=math.floor(b_c/2)
    b_a=b_a+b_c_cil
    b_b=b_b+b_c_floor
    if b_a>b_b:
        print("First")
    else:
        print("Second")

#b_a = button a ......b ...c