oparetion=int(input())
for i in range(oparetion):
    num=int(input())
    st_list=list(map(int,input().split()))
    unhappy=0
    for j in range(num):
        if st_list[j]==j+1:
            unhappy+=1
    if unhappy%2!=0:
        print((unhappy+1)//2)
    else:
        print(unhappy//2)    