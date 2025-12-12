n=int(input())
l=list(map(int,input().split()))
minn=min(l)
x=True
aa=True
if n<3:
    if n==2:
        if l[0]<l[1]:
            print("yes")
            print(1,1)
        else:
            print("yes")
            print(1,2)
    else:
        print("yes")
        print(1,1)
else:
    c=0
    s=0
    for i in range(n-1):
        if l[i]>l[i+1]:
            if aa:
                s=i
                aa=False
            c+=1
            
    m = l[s:c+1+s]
    w=[]
    for i in range(len(m)-1,-1,-1):
        w.append(m[i])
    # print(w)
    m = l[:s] + w + l[c+1+s:]
    # print(m)
    for i in range(len(m)-1):
        if m[i]>m[i+1]:
            x=False
            break
        
    if x:
        print("yes")
        print(s+1,c+1+s)
    else:
        print("no")
    
