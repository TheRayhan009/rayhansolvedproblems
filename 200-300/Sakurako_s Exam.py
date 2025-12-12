n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if a==0 and b%2!=0:
        print("NO")
    elif b==0 and a%2!=0:
        print("NO")
    else:
        check=False
        extra_2=False
        if b%2!=0 and b!=0:
            extra_2=True
        
        if extra_2:
            if a>1:
                a-=2
        if a%2==0:
            print("YES")
        else:
            print("NO")