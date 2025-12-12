oparetion=int(input())
for i in range(oparetion):
    list_len=int(input())
    num_list=[]
    for j in range(1,list_len+1):
        num_list.append(j)
    if list_len%2!=0:
        for x in range(0,list_len-1,2):
            num_list[x],num_list[x+1] = num_list[x+1] , num_list[x]
        num_list[x],num_list[-1] = num_list[-1] , num_list[x]
    if list_len%2==0:
        for x in range(0,list_len-1,2):
            num_list[x],num_list[x+1] = num_list[x+1] , num_list[x]
    print(*num_list,sep=" ")
        