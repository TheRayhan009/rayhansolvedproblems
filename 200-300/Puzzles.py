n,m=map(int,input().split())
l=list(map(int,input().split()))
l.sort(reverse=True)
minx=1000000000000
for i in range(0,(m-n)+1):
    minx=min( max(l[i:i+n]) - min(l[i:i+n]),minx )
    
print(minx)