oparetion=int(input())
for i in range(oparetion):
    lenth=int(input())
    num_list=list(map(int,input().split()))
    max_num=max(num_list)
    max_index=num_list.index(max_num)
    if num_list[-1]!=max_num:
        x=0
        if num_list[max_index-1]>=num_list[max_index+1]:
            x=num_list[max_index-1]
        if num_list[max_index-1]<=num_list[max_index+1]:
            x=num_list=num_list[max_index+1]
    else:
        x=num_list[max_index-1]
    print(x*max_num)
    