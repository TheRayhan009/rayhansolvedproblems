n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    if x<y:
        print("No")
    else:
        y=y-x
        if y%2==0:
            print("YES")
        else:
            print("No")