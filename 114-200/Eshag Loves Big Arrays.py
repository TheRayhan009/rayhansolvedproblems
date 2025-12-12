oparetion=int(input())
for i in range(oparetion):
    num_list_len=int(input())
    num_list=list(map(int,input().split()))
    num_list.sort()
    ans=0
    for j in range(num_list_len):
        # print(num_list[0],num_list[-1])
        x=num_list[0]+num_list[-1]
        abg=x//2
        if abg<num_list[-1]:
            num_list.pop()
            ans+=1
        else:
            break
    print(ans)