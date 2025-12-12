oparetion=int(input())
for i in range(oparetion):
    num=list(input())
    last_chak=0
    first_chak=0
    x=True
    first_1_chak=False
    sec_1_chak=False
    first=0
    sec=0
    zero_chek=False
    lenx=len(num)
    for j in range(0,lenx):
        if x==True:
            if num[j]=="1":
                x=False
                first_1_chak=True
                first=j
                sec_1_chak=True
        if num[j]=="1":
            sec=j
    st_list=num[first:sec]
    if "0" in st_list:
        zero_chek=True
    else:
        print("0")
    if zero_chek==True:
        ans=st_list.count("0")
        print(ans)
    
    
