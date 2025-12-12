n = int(input())
for i in range(n):
    ans=0
    x,y,z=map(int,input().split())
    left_poket=list(map(int,input().split()))
    right_poket=list(map(int,input().split()))
    
    for q in range(x):
        for p in range(y):
            if left_poket[q]+right_poket[p]<=z:
                ans+=1
    print(ans)