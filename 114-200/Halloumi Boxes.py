oparetion=int(input())
for i in range(oparetion):
    n,k=map(int,input().split())
    num_list=list(map(int,input().split()))
    x_list=num_list.copy()
    # print(x_list)
    num_list.sort()
    num_set=set(num_list)
    num_set=list(num_set)
    if num_list==x_list:
        print("YES")
    elif k==1 and len(num_set)!=1:
        print("NO")
    else:
        print("YES")