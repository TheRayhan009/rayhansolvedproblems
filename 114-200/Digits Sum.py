oparetion=int(input())
for i in range(oparetion):
    num=int(input())
    lenx=len(str(num))
    ans=num//10
    x=str(num)
    if x[lenx-1]=="9":
        print(ans+1)
    else:
        print(ans)