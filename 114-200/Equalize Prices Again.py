import math
oparetion=int(input())
for i in range(oparetion):
    list_len=int(input())
    num_list=list(map(int,input().split()))
    sum=0
    for j in range(list_len):
        sum+=num_list[j]
    print(math.ceil(sum/list_len))
