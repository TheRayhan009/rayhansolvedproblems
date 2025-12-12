def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

oparetion=int(input())
for i in range(oparetion):
    list_len=int(input())
    num_list=list(map(int,input().split()))
    x=True
    # print(prime(num_list[1]))
    for j in num_list:
        if prime(j)==True:
            x=False
            break
    if x==True:
        print("YES")
    else:
        print("NO")