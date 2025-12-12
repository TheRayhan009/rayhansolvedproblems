oparetions=int(input())
for i in range(oparetions):
    num=int(input())
    z=0
    for j in range(1,num+1):
        st=str(j)
        num_max=max(str(j))
        stlen=len(str(j))
        chak=0
        for a in range(stlen):
            if st[a]==num_max:
                chak+=1
        if stlen==chak:
            z+=1
    print(z)
