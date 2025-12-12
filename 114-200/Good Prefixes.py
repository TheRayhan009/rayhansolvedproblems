#Time limit exceeded on test 3

oparetion=int(input())
for i in range(oparetion):
    num_list_len=int(input())
    num_list=list(map(int,input().split()))
    chak_list=[]
    sumx=0
    ans=0
    # chak_list.append(num_list[0])
    for j in range(0,num_list_len):
        chak_list.append(num_list[j])
        sumx=0
        if j>0:
            x=max(chak_list)
        else:
            x=0
        # chak_list.sort()
        for k in range(len(chak_list)):
            sumx+=chak_list[k]
        if sumx-x==x and num_list_len!=1:
            ans+=1
        elif sumx==0 and num_list_len==1:
            ans+=1
            # break
    print(ans)