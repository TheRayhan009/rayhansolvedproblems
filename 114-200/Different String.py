import random
oparetion=int(input())
for i in range(oparetion):
    st=input()
    st_list=list(st)
    if st_list.count(st[0])==len(st):
        print("NO")
    else:
        if st==st[::-1]:
            for x in range(len(st)):
                random.shuffle(st_list)
                if st_list!=st_list[::-1]:
                    print("YES")
                    print(*st_list,sep="")
                    break
            
        else:
            print("YES")
            print(*st_list[::-1],sep="")