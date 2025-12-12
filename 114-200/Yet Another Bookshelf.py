oparetion=int(input())
for i in range(oparetion):
    list_len=int(input())
    num_list=list(map(int,input().split()))
    ans=0
    for x in range(list_len):
        if num_list[x]==1:
            index1=x
            break
    for y in range(list_len-1,-1,-1):
        if num_list[y]==1:
            index2=y 
            break
    for t in range(index1,index2):
        if num_list[t]==0:
            ans+=1
    print(ans)