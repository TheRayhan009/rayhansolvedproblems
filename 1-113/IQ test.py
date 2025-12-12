n=int(input())
l=list(map(int,input().split()))
jor=0
bijor=0
for i in range(0,n):
    if l[i]%2==0:
        jor = jor + 1
    else:
        bijor = bijor + 1
if jor>bijor:
    
    for j in range(n):
        if l[j]%2!=0:
            ans=j
            break
else :
    for j in range(n):
        if l[j]%2==0:
            ans=j
            break
print(ans+1)