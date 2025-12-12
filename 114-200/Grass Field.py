o=int(input())
for i in range(o):
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    a=x+y
    # print(a)
    k=a.count(1)
    if k==0:
        print("0")
    elif k==1 or k==2 or k==3:
        print("1")
    else:
        print("2")