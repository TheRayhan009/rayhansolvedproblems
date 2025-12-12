oparetions=int(input())
for i in range(oparetions):
    num=int(input())
    num_list=list(map(int,input().split()))
    ans=[]
    for j in range(2,num+2):
        if j%2==0:
            ans.append(num_list[0])
            num_list.remove(num_list[0])
        elif j%2!=0:
            ans.append(num_list[-1])
            num_list.pop()
    print(* ans , sep=" ")