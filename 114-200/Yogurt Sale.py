oparetion=int(input())
for i in range(oparetion):
    n,a,b=map(int,input().split())
    x=0 
    y=0
    if n<=1:
        print(a)
    elif a*2 > b and n>1 and n%2==0:
        print((n*b)//2)
    elif a*2 > b and n>1 and n%2!=0:
        x=(n//2)*b
        y=a
        print(x+y)
    elif a*2 < b and n>1 and n%2==0:
        print(n*a)
    elif a*2 < b and n>1 and n%2!=0:
        print(n*a)
    else:
        print(n*a)