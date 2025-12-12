oparetions=int(input())
for i in range(oparetions):
    len_list,element=map(int,input().split())
    list_num=list(map(int,input().split()))
    x=0
    for j in range(len_list):
        if list_num[j]==element:
            x=1
            print("YES")
            break
    if x==0:
        print("NO")