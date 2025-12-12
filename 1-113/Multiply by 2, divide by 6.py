oparetions=int(input())
for i in range(oparetions):
    num=int(input())
    x=0
    ans=0
    len=num
    if num==1:
        print("0")
    else:
        while x<len:
            if num==1:
                print(ans)
                break
            elif num%6==0:
                num=int(num/6)
            else:
                num=num*2
                ans=ans+1
                if num%6==0:
                    num=int(num/6)
                elif num%6!=0:
                    print("-1")
                    break
            x+=1
            ans+=1