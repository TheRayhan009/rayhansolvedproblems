oparetion=int(input())
for i in range(oparetion):
    n,s,r=map(int,input().split())
    max_dai=s-r
    s=s-max_dai
    ans=[]
    ans.append(max_dai)
    for j in range(n-1):
        ans.append(1)
        s-=1
    ans.sort()
    for a in range(len(ans)-1):
        # if ans[a]<6 and s!=0:
        c=abs(max_dai-ans[a])
        if c<=s:
            ans[a]= ans[a]+c
            s=s-c
        else:
            ans[a]=ans[a]+s
            s-=s
            # s=0
        if s==0:
            break
    # ans.sort()
    print(*ans,sep=" ")