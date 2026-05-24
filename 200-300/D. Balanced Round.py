oparetion = int(input())
for i in range(oparetion):
    k,y=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    # print(l)
    prelen=len(l)
    max_count=0
    count=0
    x=0
    while x<len(l)-1:
        if l[x+1] - l[x] > y:
            if max_count<count:
                max_count=count
            count=0

        else:
            count+=1
        x+=1
        if x==len(l)-1:
            if max_count<count:
                max_count=count
                # count=0

    print(k-(max_count+1))
    # print(l)