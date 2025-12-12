l=int(input())
for i in range(l):
    a,b,c,d=map(int,input().split())
    ans=0
    if a<b:
        ans = ans + 1
    if a<c:
        ans = ans + 1
    if a<d:
        ans = ans + 1
    print(ans)