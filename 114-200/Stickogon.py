opareton=int(input())
for i in range(opareton):
    list_len=int(input())
    num_list=list(map(int,input().split()))
    num_list.sort()
    x=set(num_list)
    x=list(x)
    ans2=0
    d=num_list.count(x[0])
    f=d
    for j in range(len(x)):
        d=num_list.count(x[j])
        if f<d and d>2:
            f=d
        
        print(f)
    print(ans2)