opa=int(input())
for i in range(opa):
    count=0
    lengthx=int(input())
    num_list=list(map(int,input().split()))
    indexx=[]
    for i in range(len(num_list)):
        for j in range(i+1,len(num_list)):
            if num_list[i]>num_list[j]:
                count+=1
                indexx.append(j)
    x=set(indexx)
    # print(x)
    # x=list(indexx)
    print(len(x))