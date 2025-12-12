n = int(input())
for i in range(n):
    x,y=map(int,input().split())
    if x==y:
        print(0)

    if x-y < 0:
        if abs(x-y)%2==0:
            print(2)
        else:
            print(1)
    elif x-y > 0:
        if abs(x-y)%2==0:
            print(1)
        else:
            print(2)
            
    # solution - 2

    # else:
    #     if x%2!=0 and y%2!=0 and x<y:
    #         print(2)
    #     elif x%2!=0 and y%2!=0 and x>y:
    #         print(1)
    #     elif x%2!=0 and y%2==0 and x<y:
    #         print(1)
    #     elif x%2!=0 and y%2==0 and x>y:
    #         print(2)
    #     elif x%2==0 and y%2==0 and x<y:
    #         print(2)
    #     elif x%2==0 and y%2==0 and x>y:
    #         print(1)
    #     elif x%2==0 and y%2!=0 and x<y:
    #         print(1)
    #     elif x%2==0 and y%2!=0 and x>y:
    #         print(2)