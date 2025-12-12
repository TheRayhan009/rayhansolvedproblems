oparetions=int(input())
for i in range(oparetions):
    st=list(input())
    key_list=[]
    chak=False
    for j in range(len(st)):
        if st[j] == "r" or st[j] == "g" or st[j] == "b":
            key_list.append(st[j])
        else:
            if st[j]=="R" and "r" not in key_list:
                chak=True
                break
            elif st[j]=="G" and "g" not in key_list:
                chak=True
                break
            elif st[j]=="B" and "b" not in key_list:
                chak=True
                break
    if chak==True:
        print("NO")
    else:
        print("YES")