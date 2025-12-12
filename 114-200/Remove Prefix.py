# problem : Time limit exceeded on test 3
oparetion=int(input())
for i in range(oparetion):
    list_len=int(input())
    num_list=input().split()
    chak_list=[]
    m=0
    for j in range(list_len-1,-1,-1):
        if num_list[j] in chak_list:
            m=j+1
            break
        chak_list.append(num_list[j])
    if abs(m - list_len)==list_len:
        print("0")
    elif list_len!=1:
        print(m)
    else:
        print("0")