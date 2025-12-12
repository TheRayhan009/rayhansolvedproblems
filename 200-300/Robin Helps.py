oparations=int(input())
for i in range(oparations):
    golds_have=0
    ans=0
    a,b=map(int ,input().split())
    golds=list(map(int,input().split()))
    for j in range(len(golds)):
        if golds[j]>=b:
            golds_have+=golds[j]
        if golds[j]==0 and golds_have>0:
            ans+=1
            golds_have-=1
    print(ans)
        