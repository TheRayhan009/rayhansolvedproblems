oparations=int(input())
for i in range(oparations):
    st=input()
    st1=""
    st2=""
    x=0
    if len(st)%2!=0:
        print("NO")
    else:
        hup=int(len(st)/2)
        for j in range(0,hup):
            st1=st1+st[j]
        for k in range(hup,len(st)):
            st2=st2+st[k]
        if st1==st2:
            print("YES")
        else:
            print("NO")
        

# operations = int(input())
# for _ in range(operations):
#     st = input()
#     if len(st) % 2 != 0 or st[:len(st)//2] != st[len(st)//2:]:
#         print("NO")
#     else:
#         print("YES")
