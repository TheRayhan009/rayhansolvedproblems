num1,num2=map(int,input().split())
ans=0
prime=[]
for a in range(num1,num2+1):
    s=0
    for b in range(2,num2):
        v=a
        if a%b == 0 and b!=a:
            s=1
            break
    if s==0:
        prime.append(v)
if len(prime)<2:
    print("NO")
elif prime[1]!=num2:
    print("NO")
elif prime[1]==num2:
    print("YES")
#---------------------------------------------------------
# for i in range(num1,num2*10):
#     x=0
#     y=0
#     ans=i
#     for j in range(2,num2):
#         if i%j != 0:
#             x=x+1
#         y=y+1
#     if x==y:
#         break
