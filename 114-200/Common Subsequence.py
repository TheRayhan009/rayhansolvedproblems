oparetion=int(input())
for i in range(oparetion):
    n,k=map(int,input().split())
    num_list=list(map(int,input().split()))
    num_list2=list(map(int,input().split()))
    num_list.sort()
    num_list2.sort()
    # if 1 in num_list and len(num_list)==1 and 1 in num_list and len(num_list)==1:
    #     print("NO")
    # else:
    #     if 1 in num_list and len(num_list)!=1:
    #         num_list.remove(1)
    #     if 1 in num_list2 and len(num_list2)!=1:
    #         num_list2.remove(1)
    x=[]
    chak=False
    if n>=k:
        for j in range(n):
            if num_list[j] in num_list2 and num_list[j]!=1:
                x.append(num_list[j])
            if len(x)>0:
                chak=True
                break
    else:
        for j in range(k):
            if num_list2[j] in num_list and num_list2[j]!=1:
                x.append(num_list2[j])
            if len(x)>0:
                chak=True
                break
    if num_list.count(1)>1 or num_list2.count(1)>1:
        print("YES")
        print("1 1")
    elif chak==True:
        if 1 not in x:
            x.append(1)
        x.sort()
        # print(x)
        # x.pop()
        print("YES")
        print(*x,sep=" ")
        # else:
        #     print("YES")
        #     print(*x,sep=" ")
    else:
        print("NO")