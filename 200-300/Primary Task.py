n=int(input())
for i in range(n):
    st_num=str(input())
    if len(st_num)>2:
        if st_num[0]+st_num[1]=="10":
            if int(st_num[2::]) >= 2 and st_num[2]!="0":
                print("YES")
            else:
                print("NO")
        else:  
            print("NO")
    else:
        print("NO")