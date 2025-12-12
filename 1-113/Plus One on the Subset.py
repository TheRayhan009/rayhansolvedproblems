oparations=int(input())
for i in range(oparations):
    line=int(input())
    eliments=list(map(int,input().split()))
    x=min(eliments)
    y=max(eliments)
    print(y-x)
