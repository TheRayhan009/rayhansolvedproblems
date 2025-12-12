ls=int(input())
ans=0
f=0
for i in range(ls):
    a,b=map(int ,input().split())
    f=ans
    ans=abs((ans-a)+b)
    if ans>=f:
            ans1=ans
print(ans1)
# 4
# 4-4=0+6=6  // 6
# 6-6=0+5=5  // 5
# 5-5=0+4=4
# 
