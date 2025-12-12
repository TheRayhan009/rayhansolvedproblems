oparetion=int(input())
for i in range(oparetion):
    lenth,ram=map(int,input().split())
    a_list=list(map(int,input().split()))
    b_list=list(map(int,input().split()))
    for j in range(lenth):
        min_num=min(a_list)
        index=a_list.index(min_num)
        if a_list[index]<=ram:
            ram+=b_list[index]
            del a_list[index]
            del b_list[index]
        else:
            break
    print(ram)
        