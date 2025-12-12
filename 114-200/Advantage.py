oparetions=int(input())
for i in range(oparetions):
    num_list_len=int(input())
    num_list=list(map(int,input().split()))
    ans=[]
    secund_max_num_of_list=0
    same_list=num_list.copy()
    max_num_of_list=max(num_list)
    same_list.sort(reverse=False)
    secund_max_num_of_list=same_list[-2]
    for j in range(len(num_list)):
        if num_list[j]==max_num_of_list:
            x=num_list[j]-secund_max_num_of_list
            ans.append(x)
        else:
            x=num_list[j]-max_num_of_list
            ans.append(x)
    print(*ans,sep=" ")