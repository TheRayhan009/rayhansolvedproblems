opa=int(input())
for i in range(opa):
    num_list=list(map(int,input().split()))
    if num_list[0]==num_list[1]==num_list[2]==num_list[3]:
        print("YES")
    else:
        print("No")