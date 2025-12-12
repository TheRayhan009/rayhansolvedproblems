a,b=map(int,input().split())
x=b-1
even=[]
odd=[]
for i in range(1,a+1):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
ans=odd+even
print(ans[x])