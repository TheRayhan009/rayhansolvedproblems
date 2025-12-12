oparetion=int(input())
for i in range(oparetion):
    list_len=int(input())
    num_list=list(map(int,input().split()))
    odd_list=[]
    even_list=[]
    for j in range(list_len):
        if num_list[j]%2==0:
            even_list.append(num_list[j])
        else:
            odd_list.append(num_list[j])
    even_list.sort()
    odd_list.sort()
    for x in range(list_len):
        if num_list[x]%2!=0:
            