oparation=int(input())
for i in range(oparation):
    st_len=int(input())
    st=input()
    st_list=[]
    st_contenar=[]
    for x in range(0,st_len-1):
        marg=st[x]+st[x+1]
        st_list.append(marg)
    for j in range(len(st_list)):
        if st_list[j] not in st_contenar:
            st_contenar.append(st_list[j])
    print(len(st_contenar))