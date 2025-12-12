oparetion=int(input())
for i in range(oparetion):
    sts=int(input())
    full_st=""
    chak=[]
    all_chak=True
    for j in range(sts):
        st=input()
        full_st+=st
    full_set=set(full_st)
    full_set=list(full_set)
    for q in range(len(full_set)):
        x=full_st.count(full_set[q])
        chak.append(x)
    for s in range(len(chak)):
        if chak[s]%sts!=0:
            all_chak=False
            break
    if all_chak==True:
        print("YES")
    else:
        print("NO")