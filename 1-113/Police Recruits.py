cases=int(input())
oparations=list(map(int,input().split()))
haveing_police = 0
ans=0
for i in range(cases):
    if haveing_police == 0 and oparations[i]==-1:
        ans = ans + 1
    elif haveing_police > 0 and oparations[i]==-1:
        haveing_police = haveing_police - 1
    else:
        haveing_police = haveing_police + oparations[i]
print(ans)