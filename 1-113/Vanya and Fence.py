a,b=map(int,input().split())
l=list(map(int,input().split()))
point=0
for j in range(a):
    if l[j]<=b:
        point=point+1
    else:
        point=point+2
print(point)