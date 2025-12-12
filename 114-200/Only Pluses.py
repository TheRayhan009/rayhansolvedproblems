c=int(input())
for i in range(c):
    l=list(map(int,input().split()))
    for j in range(5):
        l.sort()
        l[0]+=1
    print(l[0]*l[1]*l[2])