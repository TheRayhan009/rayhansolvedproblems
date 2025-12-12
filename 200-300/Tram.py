ls=int(input())
ans=0
f=0
x=True
for i in range(ls):
    a,b=map(int ,input().split())
    ans=abs((ans-a))+b
    if ans>=f:
        ans1=ans
        f=ans

print(ans1)