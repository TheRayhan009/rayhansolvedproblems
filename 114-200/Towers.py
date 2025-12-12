list_len=int(input())
num_list=list(map(int,input().split()))
set_list=set(num_list)
chak=0
for i in set_list:
    if num_list.count(i)>chak:
        chak=num_list.count(i)
print(chak , len(set_list))