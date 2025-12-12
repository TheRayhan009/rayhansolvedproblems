n=int(input())
for i in range(n):
    x=int(input())
    l1=input()
    l2=input()
    # if l1[0]!="0":
    #     print("NO")
    # else:
    l=True
    for j in range(1,x):
        if l1[j]=="1":
            l=False
            for k in range(j):
                if l2[k]=="0":
                    l2[k]=="1"
                    l=True
                    break
        if l==False:
            print("NO")
            break
    if l==True:
        print("YES")
        
        