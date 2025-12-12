a,b=map(int,input().split())
for row in range(a*b):
    if row/b==0:
        print("\n")
    print("#",end=" ")
