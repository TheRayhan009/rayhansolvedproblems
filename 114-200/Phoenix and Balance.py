oparetions=int(input())
for i in range(oparetions):
    num=int(input())
    for j in range(num):
        wate=[]
        for x in range(1,num+1):
            wate.append(2**x)
        wate.sort()
        d=0
        ans=0
        z=0
        ans_list=[]
        if len(wate)==2:
            ans=wate[-1]-wate[0]
        else:
            for a in range(0,int(num/2)):
                s=wate[0]+wate[-1]
                ans_list.append(s)
                wate.remove(wate[0])
                wate.pop()
            for q in range(0,len(ans_list)-1,2):
                d=ans_list[q]
                n=ans_list[q+1]
                z=d-n-z
    print(z)