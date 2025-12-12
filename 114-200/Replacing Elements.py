oparetions=int(input())
for i in range(oparetions):
    list_len,num_need=map(int,input().split())
    num_list=list(map(int,input().split()))
    # num_list=set(num_list)
    # num_list=list(num_list)
    num_list.sort()
    sum=num_list[0]+num_list[1]
    if num_list[-1]<=num_need:
        print("YES")
    elif sum<=num_need:
        print("YES")
    else:
        print("NO")