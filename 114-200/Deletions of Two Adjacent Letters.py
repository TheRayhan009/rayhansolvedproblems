oparetions=int(input())
for i in range(oparetions):
    st=input()
    letter=input()
    st_list=list(st)
    st_list_len=len(st_list)
    st_list_el_mid=len(st_list)//2
    if st_list[st_list_el_mid]==letter:
        print("YES")
    else:
        print("NO")
    
    