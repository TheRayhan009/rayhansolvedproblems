oparetion=int(input())
for i in range(oparetion):
    num=input()
    x=""
    for j in range(len(x)-1):
        x=x+"0"
    # print(str(x))
    c=int(num)-int(num[0]+x)
    num=num[0]+x
    print
    print(num,c)
    