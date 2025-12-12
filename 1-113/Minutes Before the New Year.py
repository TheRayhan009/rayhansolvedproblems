opqrations=int(input())
for i in range(opqrations):
    hour,minute=map(int,input().split())
    sum=0
    x=1440
    hour=hour*60
    sum=hour+minute
    print(x-sum)