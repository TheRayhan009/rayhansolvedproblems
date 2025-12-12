oparetions=int(input())
for i in range(oparetions):
    st=input()
    st_list=[]
    for a in range(len(st)):
        st_list.append(st[a])
    real_st=['a','b','c']
    if st_list==real_st:
        print("YES")
    else:
        chak_list=[]
        for j in range(3):
            if real_st[j]!=st_list[j]:
                chak_list.append(st[j])
        if len(chak_list)==3:
            print("NO")
        else:
            print("YES")
        