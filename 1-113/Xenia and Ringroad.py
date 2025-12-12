ring_road_len,houses=map(int,input().split())
num_house=list(map(int,input().split())) 
carent_house=1
ans=0
for i in range(houses):
    for j in range(num_house[i]):
        if carent_house<num_house[i]:
            ans=ans+1
            carent_house=carent_house+1
            if carent_house>ring_road_len:
                carent_house=1
        elif carent_house==num_house[i]:
            ans=ans+1
            if carent_house>ring_road_len:
                carent_house=1
print(ans)

"""
4 3
3 2 3

"""