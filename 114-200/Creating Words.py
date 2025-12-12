o=int(input())
for i in range(o):
    a,b=map(str,input().split())
    x=a[0]
    y=b[0]
    a=y+a[1:]
    b=x+b[1:]
    print(a,b)