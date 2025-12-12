n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    max_count=0
    last_NUM_check=0
    l.append(b)
    l.insert(0,0)
    # print(l)
    
    for i in range(0,len(l)-1):
        max_count=max(max_count,abs(l[i+1]-l[i]))
    
    last_NUM_check= abs(l[-2]-l[-1]) * 2
    
    print(max(last_NUM_check,max_count))