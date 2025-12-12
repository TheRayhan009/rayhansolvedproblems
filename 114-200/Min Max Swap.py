oparetion=int(input())
for i in range(oparetion):
    lenth=int(input())
    min_list=list(map(int,input().split()))
    max_list=list(map(int,input().split()))
    for j in range(lenth):
        if min_list[j]>max_list[j]:
            max_list[j],min_list[j]=min_list[j],max_list[j]
    min_list_max_num=max(min_list)
    max_list_max_num=max(max_list)
    print(min_list_max_num*max_list_max_num)