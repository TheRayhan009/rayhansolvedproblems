oparetions=int(input())
for i in range(oparetions):
    a,b=map(int,input().split())
    if a==0 and b!=0:
        print("1")
    else:
        BDT_1_coin=a*1
        BDT_2_coin=b*2
        sum=BDT_1_coin + BDT_2_coin
        print(sum+1)