oparetion=int(input())
for i in range(oparetion):
    num=int(input())
    alpa=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    if num%2!=0:
        print("NO")
    else:
        print("YES")
        ans=""
        j=0
        x=j
        for j in range(num//2):
            if x==25:
                x=0
            ans+=alpa[x]
            ans+=alpa[x]
            x+=1
        print(ans)
        