oparetions=int(input())
for i in range(oparetions):
    num=int(input())
    num_list=list(map(int,input().split()))
    even=0
    odd=0
    for j in range(len(num_list)):
        if num_list[j]%2==0:
            even+=1
        elif num_list[j]%2!=0:
            odd+=1
    if odd==even:
        if int((odd+even) / 2 )== num:
            print("Yes")
        else:
            print("No")
    else:
        print("No")