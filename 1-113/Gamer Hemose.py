oparations=int(input())
for i in range(oparations):
    weapons,health=map(int,input().split())
    len=health
    ans=0
    weapons_power=list(map(int,input().split()))
    weapons_power.sort(reverse=True)
    weapons1=weapons_power[0]
    weapons2=weapons_power[1]
    for j in range(1,len+1):
        if health<=0:
            break
        elif j % 2 != 0:
            ans=ans+1
            health=health-weapons1
        elif j % 2 == 0:
            ans=ans+1
            health=health-weapons2
    print(ans)

