oparetion=int(input())
for i in range(oparetion):
    num=int(input())
    if num==1:
        print("2")
    elif num%3==1 or num%3==2:
        print((num//3)+1)
    else:
        print(num//3)