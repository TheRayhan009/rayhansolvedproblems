oparetion=int(input())
for i in range(oparetion):
    a,b,c,n=map(int,input().split())
    sum=a+b+c+n
    if sum%3==0:
        if a>sum//3 or b>sum//3 or c>sum//3:
            print("NO")
        else:
            print("YES")
    else:
        print("NO")