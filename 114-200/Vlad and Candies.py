oparetion=int(input())
for i in range(oparetion):
    list_len=int(input())
    num_list=list(map(int,input().split()))
    if list_len==1:
        if num_list[0]==1:
            print("YES")
        else:
            print("NO")
    else:
        x=False
        num_list.sort()
        if num_list[-1]-num_list[-2]>1:
            print("NO")
        else:
            print("YES")