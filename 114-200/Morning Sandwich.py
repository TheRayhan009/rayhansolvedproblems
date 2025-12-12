oparetion=int(input())
for i in range(oparetion):
    a,b,c=map(int,input().split())
    sumx=b+c
    ans=0
    if a==2 and sumx>0:
        print("3")
    else:
        a-=1
        while True:
            if a>=1 and sumx>=1:
                a-=1
                sumx-=1
                ans+=1
            else:
                break
        print((ans*2)+1)