n=int(input())
for i in range(n):
    a=int(input())
    st=input()
    l_1=[]
    l_0=[]
    check=True
    for i in range(a):
        if st[i] in l_1 or st[i] in l_0:
            
            if i%2==0 and st[i] not in l_1:
                check=False
                break
            if i%2!=0 and st[i] not in l_0:
                check=False
                break
        else: 
            if i%2==0:
                l_1.append(st[i])
            else:
                l_0.append(st[i])
            
    if check:
        print("YES")
    else:
        print("NO")