oparetions=int(input())
for i in range(oparetions):
    apartment,rooms=map(int,input().split())
    floor=0
    for j in range(0,apartment,rooms):
        if j>=apartment:
            floor=floor+1
            break
        floor=floor+1
    print(floor)