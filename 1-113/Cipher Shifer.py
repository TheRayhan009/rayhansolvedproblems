#unsolved
oparation=int(input())
for i in range(oparation):
    st_len=int(input())
    st=input()
    st_set=list(st)
    a=[]
    for x in range(0,len(st_set)-1):
        if st_set[x] != st_set[x+1]:
            a.append(st_set[x])
    a.append(st_set[-1])
    # st_set=list(a)
    # ans=[]
    # for j in st:
    #     if j in st_set:
    #         ans.append(j)
    #         st_set.remove(j)
    print(''.join(a))
    
