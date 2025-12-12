lenn=int(input())
num_list=list(map(int,input().split()))
l=[]
x=""
for i in range(lenn-1,-1,-1):
    if num_list[i] not in l:
        l.append(num_list[i])
        x=str(num_list[i])+" "+x
print(len(l))
print(x)