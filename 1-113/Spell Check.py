oparation=int(input())

for i in range(oparation):
    st_len=int(input())
    st=input()
    st_list=[]
    ans=0
    y=0
    for x in range(len(st)):
        st_list.append(st[x])
    st_chak=['T', 'i', 'm', 'u', 'r']
    for j in range(len(st)):
        if st_list[j] in st_chak:
            st_chak.remove(st_list[j])
            ans=ans+1
        else:
            print("NO")
            break
    if len(st)==ans and st_len==5:
        print("YES")
