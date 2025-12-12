oparetion=int(input())
for i in range(oparetion):
    list_len=int(input())
    num_list=list(map(int,input().split()))
    even=[]
    odd=[]
    ans=[]
    for j in num_list:
        if j%2==0:
            even.append(j)
        else:
            odd.append(j)
    # xlen=max(len(even),len(odd))
    if len(even)>len(odd):
        for k in range(len(even)):
            ans.append(even[k])
            # ans.append(odd[k])
        for q in range(len(odd)):
            # ans.append(even[k])
            ans.append(odd[q])
    else:
        for k in range(len(odd)):
            # ans.append(even[k])
            ans.append(odd[k])
        for q in range(len(even)):
            ans.append(even[q])
            # ans.append(odd[k])
    # if len(even)!=len(odd):
    #     if len(even)>len(odd):
    #         ans.append(even[len(even)-len(odd):-1])
    #     else:
    #         ans.append(odd[len(odd)-len(even):-1])
    print(*ans,sep=" ")