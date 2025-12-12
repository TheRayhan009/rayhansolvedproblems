total_level=int(input())
x_list=list(map(int,input().split()))
y_list=list(map(int,input().split()))
x_sub_list=x_list[1:]
y_sub_list=y_list[1:]

sum_of_list=x_sub_list+y_sub_list
sum_of_list=set(sum_of_list)
sum_of_list=list(sum_of_list)
sum_of_list.sort()
x=1
test=False
for i in range(len(sum_of_list)):
    if sum_of_list[i]==x and len(sum_of_list)==total_level:
        test=True
    else:
        test=False
        break
    x+=1
if test==True:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")

