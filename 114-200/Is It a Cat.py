oparetion=int(input())
for i in range(oparetion):
    st_len=int(input())
    st=input()
    M_chak=False
    E_chak=False
    O_chak=False
    W_chak=False
    # index_chak=False
    all_chak=False
    next=False
    M=True
    E=True
    O=True
    # W=True
    for j in st:
        if next==False:
            if j.lower()=="a" or j.lower()=="b"  or j.lower()=="c"  or j.lower()=="d"  or j.lower()=="f"  or j.lower()=="g"  or j.lower()=="h"  or j.lower()=="i"  or j.lower()=="j"  or j.lower()=="k"  or j.lower()=="l"  or j.lower()=="n"  or j.lower()=="p"  or j.lower()=="q"  or j.lower()=="r"  or j.lower()=="s"  or j.lower()=="t"  or j.lower()=="u"  or j.lower()=="v"  or j.lower()=="x"  or j.lower()=="y"  or j.lower()=="z" :
                all_chak=True
                break
            
            if j=="M" or j=="m" and M==True:
                M_chak=True
            elif j=="E" and M_chak==True and E==True:
                M=False
                E_chak=True
            elif j=="e" and M_chak==True and E==True:
                M=False
                E_chak=True
            elif j=="O" and M_chak==True and E_chak==True and O==True:
                E=False
                O_chak=True
            elif j=="o" and M_chak==True and E_chak==True and O==True:
                E=False
                O_chak=True
            elif j=="w" and M_chak==True and E_chak==True and O_chak==True:
                O=False
                W_chak=True
                next=True
            elif j=="W" and M_chak==True and E_chak==True and O_chak==True:
                O=False
                W_chak=True
                next=True
            else:
                all_chak=True
                break
        if next==True:
            if j.lower()!="w" :
                all_chak=True
                break
    if all_chak==True:
        print("NO")
    elif M_chak==True and E_chak==True and O_chak==True and W_chak==True:
        print("YES")
    else:
        print("NO")