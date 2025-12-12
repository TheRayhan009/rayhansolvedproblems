oparetions=int(input())
for i in range(oparetions):
    st=input()
    chak_list=[]
    ans=0
    for j in range(len(st)):
        if st[j] not in chak_list:
            chak_list.append(st[j])
            x=len(chak_list)
        if len(chak_list)>3:
            ans+=1
            chak_list=[]
            chak_list.append(st[j])
    if x>0:
        print(ans+1)
    else:
        print(ans)
    