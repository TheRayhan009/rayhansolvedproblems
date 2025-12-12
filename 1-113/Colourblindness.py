oparetions=int(input())
for i in range(oparetions):
    num=int(input())
    st_list_1=input()
    st_list_2=input()
    same=0
    for j in range(num):
        if st_list_1[j]==st_list_2[j]:
            same+=1
        elif st_list_1[j]=="G" and st_list_2[j]=="B":
            same+=1
        elif st_list_1[j]=="B" and st_list_2[j]=="G":
            same+=1
    if same==num:
        print("YES")
    else:
        print("NO")
