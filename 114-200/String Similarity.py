oparetion=int(input())
for i in range(oparetion):
    sub_st_num=int(input())
    st=input()
    x=0
    ans=[]
    for j in range(sub_st_num):
        n=st[j:j+sub_st_num]
        # print(n)
        ans.append(n[j])
        # x+=1
    print(*ans,sep="")