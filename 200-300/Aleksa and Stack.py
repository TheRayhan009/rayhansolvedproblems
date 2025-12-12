n=int(input())
for i in range(n):
    a=int(input())
    x=1
    for j in range(1,a+1):
        print(x,end=" ")
        x=x + (x+1)
    print()