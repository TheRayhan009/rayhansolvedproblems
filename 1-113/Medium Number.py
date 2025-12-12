import statistics
ls = int(input())
for i in range(ls):
    a,b,c=map(int,input().split())
    x=statistics.median([a,b,c])
    print(x)
