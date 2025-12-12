n=int(input())
for i in range(n):
    x=int(input())
    if x==1:
        print(0)
    elif x==2:
        print(1)
    else:
        # l=0
        # f=x
        # for j in range(x-1,0,-1):
        #     f=f&j
        #     if f==0:
        #         print(j)
        #         break
        #         # print(f)
        c=0
        a=1
        while x>a:
            c=a
            a=(a*2)+1
        print(c)
        
