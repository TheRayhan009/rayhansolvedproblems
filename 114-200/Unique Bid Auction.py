#problem : Time limit exceeded on test 2
oparetion=int(input())
for i in range(oparetion):
    list_len=int(input())
    num_list=list(map(int,input().split()))
    chak_list=set(num_list)
    chak_list=list(chak_list)
    U_bid_num_list=[]
    for j in range(len(chak_list)):
        y=num_list.count(chak_list[j])
        if y==1:
            U_bid_num_list.append(chak_list[j])
    if len(U_bid_num_list)==0:
        print("-1")
    else:
        x=min(U_bid_num_list)
        print(num_list.index(x)+1)