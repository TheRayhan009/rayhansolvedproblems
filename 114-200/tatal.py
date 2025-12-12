number=int(input())
num_list=str(number)
lenx=0
for j in range(len(num_list)):
    if num_list[j]=="1" or num_list[j]=="4":
        lenx+=1
a=0
chak=False
if lenx==len(str(number)):
    chak=True
    x=0
    st=str(number)
    if st[0]!="1":
        chak=False
        print("NO")
        
    else:
        tow_4_chak=True
        for i in range(0,len(str(number))):
            if x>2:
                print("NO")
                a=1
                break
            elif st[i]=="1":
                x=0
            elif st[i]=="4":
                x+=1
            if x>2:
                print("NO")
                a=1
                break
    if a==0 and chak==True:
        print("YES")
else:
    print("NO")