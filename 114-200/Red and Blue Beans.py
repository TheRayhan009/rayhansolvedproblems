oparetion=int(input())
for i in range(oparetion):
    r,b,d=map(int,input().split())
    if r==b:
        print("YES")
    else:
        if abs(r-b) >= d:
            x=min(r,b)
            x=x*abs(r-b)
            if x>max(r,b):
                print("YES")
            else:
                print("NO")
        else:
            print("NO")