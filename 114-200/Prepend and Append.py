oparetions=int(input())
for i in range(oparetions):
    num=int(input())
    st=input()
    st_list=[]
    for j in range(len(st)):
        st_list.append(st[j])
    for a in range(len(st)-1):
        if len(st_list)==0:
            break
        elif st_list[0]!=st_list[-1]:
            st_list.remove(st_list[0])
            st_list.pop()
        else:
            break
    print(len(st_list))