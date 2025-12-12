oparetions=int(input())
for i in range(oparetions):
    st_len=int(input())
    st=input()
    st_list=[]
    blanck_list=[]
    ans=0
    for j in range(st_len):
        st_list.append(st[j])
    for z in range(len(st_list)):
        if st_list[z] not in blanck_list:
            blanck_list.append(st_list[z])
            ans=ans+2
        elif st_list[z] in blanck_list:
            ans=ans+1
    print(ans)
