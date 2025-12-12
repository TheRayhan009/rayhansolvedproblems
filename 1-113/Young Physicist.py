oparetion=int(input())
ans_x=0
ans_y=0
ans_z=0
for i in range(oparetion):
    x,y,z=map(int,input().split())
    ans_x=ans_x + x
    ans_y=ans_y + y
    ans_z=ans_z + z
if ans_x==0 and ans_y==0 and ans_z==0:
    print("YES")
else:
    print("NO")

