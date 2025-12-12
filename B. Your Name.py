opa=int(input())
for i in range(opa):
    lengthx=int(input())
    num_list=list(map(str,input().split()))
    # num_list2=list(map(int,input().split()))
    x=set(num_list[0])
    x=list(x)
    # num_list[0]=list(x)
    cheack=True
    for i in range(len(x)):
        if num_list[0].count(x[i]) != num_list[1].count(x[i]):
            cheack=False
            break
    if cheack:
        print("YES")
    else:
        print("NO")