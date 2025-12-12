oparetion=int(input())
for i in range(oparetion):
    number=int(input())
    if (number+1)%3==0 or (number-1)%3==0 :
        print("First")
    else:
        print("Second")