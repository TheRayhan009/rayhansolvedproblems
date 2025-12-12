oparetion=int(input())
for i in range(oparetion):
    l_len=int(input())
    num_list=list(map(int,input().split()))
    color=0
    while True:
        # num_list.sort()
        x=num_list[0]
        num_list.remove(num_list[0])
        # print(len(num_list))
        color+=1
        y=[]
        for j in range(len(num_list)):
            # print(num_list)
            if x<num_list[j]:
                # print(num_list)
                x=num_list[j]
                # print(num_list[j])
                y.append(num_list[j])
        for k in range(len(y)):
            # print(y)
            num_list.remove(y[k])
        if len(num_list)==0:
            break
        
        
    print(color)