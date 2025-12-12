# problem : Time limit exceeded
oparations=int(input())
for j in range(oparations):
    num1,div,num2=map(int,input().split())
    ans=0
    i=num2
    while True:
        if i%num1==div:
            print(i)
            break
        i=i-1