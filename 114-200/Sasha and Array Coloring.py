oparetions=int(input())
for i in range(oparetions):
    num_list_len=int(input())
    x=num_list_len
    num_list=list(map(int,input().split()))
    num_list.sort()
    ans=0
    pos_num=0
    neg_num=1
    for j in range(num_list_len//2):
        x=x-1
        ans=ans+num_list[x]-num_list[j]
    print(ans)