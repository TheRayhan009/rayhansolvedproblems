oparetion=int(input())
for i in range(oparetion):
    num=int(input())
    x=num
    ans=[]
    while x>0:
        if x>=9:
            x-=9
            ans.append("9")
        elif x>=8:
            x-=8
            ans.append("8")
        elif x>=7:
            x-=7
            ans.append("7")
        elif x>=6:
            x-=6
            ans.append("6")
        elif x>=5:
            x-=5
            ans.append("5")
        elif x>=4:
            x-=4
            ans.append("4")
        elif x>=3:
            x-=3
            ans.append("3")
        elif x>=2:
            x-=2
            ans.append("2")
        elif x>=1:
            x-=1
            ans.append("1")
        
    ans.sort()
    print(*ans,sep="")