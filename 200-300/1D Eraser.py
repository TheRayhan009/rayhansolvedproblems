n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    l=list(input())
    # print(l)
    count=0
    check=False
    for i in range(0,a):
        if l[i]=="B":
            count+=1
            for j in range(i,i+b):
                if j==a:
                    check=True
                    break
                # print(i)
                if l[j]=="B" :
                    l[j]="W"
                # print(l)
        if check:
            break
    print(count)
                