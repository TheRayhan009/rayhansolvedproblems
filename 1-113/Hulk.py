l=int(input())
if l==1:
    print("I hate it",end=" ")
else:
    for i in range(1,l+1):
        if i==l:
            if l%2==0:
                print("I love it",end=" ")
            else:
                print("I hate it",end=" ")
        elif i%2==0:
            print("I love that",end=" ")
        else:
            print("I hate that",end=" ")
