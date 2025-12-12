oparetion=int(input())
for i in range(oparetion):
    p_a=list(map(int,input().split()))
    p_b=list(map(int,input().split()))
    x=True
    if p_a[0] < p_a[1] and p_b[0] < p_b[1] and p_a[0] < p_b[0] and p_a[1] < p_b[1]:
        print("YES")
        x=False
    else:
        for s in range(3):
            p_a[0] , p_a[1] , p_b[0] , p_b[1] = p_b[0] , p_a[0] , p_b[1] , p_a[1]
            if p_a[0] < p_a[1] and p_b[0] < p_b[1] and p_a[0] < p_b[0] and p_a[1] < p_b[1]:
                print("YES")
                x=False
                break
    if x==True:
        print("NO")