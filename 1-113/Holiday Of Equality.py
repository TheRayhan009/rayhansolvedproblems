l=int(input())
money=list(map(int,input().split()))
x=max(money)
ans=0
for i in range(l):
    ans= ans + (x-money[i])
print(ans)