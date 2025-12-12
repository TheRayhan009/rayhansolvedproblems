num_len=int(input())
num_list=list(map(int,input().split()))
num_set=set(num_list)
num_set=list(num_set)
chak=0
for i in range(len(num_set)):
    x=num_list.count(num_set[i])
    if chak<x:
        chak=x
print(chak)