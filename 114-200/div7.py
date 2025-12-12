oparetions=int(input())
for i in range(oparetions):
    num=input() #as a string
    if int(num)%7==0: 
        print(num)
    else:
        num=list(num)
        num[-1]="0"
        num=''.join(num)
        num=int(num)
        while True:
            if num%7==0:
                print(num)
                break
            else:
                num+=1

