oparetion=int(input())
for i in range(oparetion):
    st_len=int(input())
    st=input()
    st=list(st)
    c_list=st
    # print(c_list)
    st=[]
    for q in range(len(c_list)):
        if c_list[q] not in st:
            st.append(c_list[q])
    # print(st)
    x=0
    final_ans=0
    for j in range(len(st)):
        ans=0
        if st[j]=="A":
            x=1
        if st[j]=="B":
            x=2
        if st[j]=="C":
            x=3
        if st[j]=="D":
            x=4
        if st[j]=="E":
            x=5
        if st[j]=="F":
            x=6
        if st[j]=="G":
            x=7
        if st[j]=="H":
            x=8
        if st[j]=="I":
            x=9
        if st[j]=="J":
            x=10
        if st[j]=="K":
            x=11
        if st[j]=="L":
            x=12
        if st[j]=="M":
            x=13
        if st[j]=="N":
            x=14
        if st[j]=="O":
            x=15
        if st[j]=="P":
            x=16
        if st[j]=="Q":
            x=17
        if st[j]=="R":
            x=18
        if st[j]=="S":
            x=19
        if st[j]=="T":
            x=20
        if st[j]=="U":
            x=21
        if st[j]=="V":
            x=22
        if st[j]=="W":
            x=23
        if st[j]=="X":
            x=24
        if st[j]=="Y":
            x=25
        if st[j]=="Z":
            x=26

        
        for v in range(st_len):
            if st[j]==c_list[v]:
                ans+=1
        if ans>=x:
            final_ans+=1
    print(final_ans)
        