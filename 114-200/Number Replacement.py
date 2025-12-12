oparetion=int(input())
for i in range(oparetion):
    num_len=int(input())
    num_list=list(map(int,input().split()))
    st_list=list(input())
    # st_list=st_list
    all_chak=False
    chak_list=[]
    for j in range(len(num_list)):
        x=st_list[j]
        y=num_list[j]
        chak_list.append(num_list[j])
        for k in range(num_len):
            # print(st_list)
            # print(st_list[k])
            if num_list[k]==y and st_list[k]!=x:
                all_chak=True
                break
        if all_chak==True:
            break
    if all_chak==True:
        print("NO")
    else:
        print("YES")