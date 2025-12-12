oparetion=int(input())
for i in range(oparetion):
    list_len=int(input())
    num_list=list(map(int,input().split()))
    x=num_list.count(2)
    if x%2==0:
        y=x//2 #3
        for j in range(list_len):
            if num_list[j]==2:
                y-=1
            if y==0:
                print(j+1)
                break
    else:
        print("-1")