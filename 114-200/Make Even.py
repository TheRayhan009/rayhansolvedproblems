oparetion=int(input())
for i in range(oparetion):
    number=input()
    chak=False
    even_index=0
    for j in range(len(number)):
        if int(number[j])%2==0:
            chak=True
            break
    if chak==False:
        print("-1")
    elif int(number[-1])%2==0:
        print("0")
    elif int(number[0])%2==0:
        print("1")
    else:
        print("2")