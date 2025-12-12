oparetions=int(input())
for i in range(oparetions):
    boxes=int(input())
    candis=list(map(int,input().split()))
    minimum_candi=min(candis)
    ans=0
    for j in range(len(candis)):
        ans=ans+(candis[j]-minimum_candi)
    print(ans)