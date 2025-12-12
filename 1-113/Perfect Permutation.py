num=int(input())
num_list=[]
if num%2!=0:
    print("-1")
else:
    for i in range(1,num+1):
        num_list.append(i)
    for j in range(0,len(num_list)-1,2):
        a1=num_list[j]
        a2=num_list[j+1]
        num_list[j]=a2
        num_list[j+1]=a1
        # print(num_list)

        # num_list[j], num_list[j+1] = num_list[j+1], num_list[j]  

    print(*num_list,sep=" ")