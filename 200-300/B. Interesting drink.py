# shops=int(input())
# num_list=list(map(int,input().split()))
# num_list.sort()
# # print(num_list)
# days=int(input())
# for i in range(days):
#     x=int(input())
#     start=0
#     end=shops-1

#     if num_list[0]>x:
#         print(0)
#     elif num_list[-1]<=x:
#         print(shops)
#     elif x not in num_list:
#         while start<=end:
#             opa = (start+end)//2
#             if num_list[opa]<x and num_list[opa+1]>x:
#                 print(opa+1)
#                 break
#             elif num_list[opa]<x:
#                 start=opa+1
#             else:
#                 end=opa-1
#     else:
#         while start<=end:
#             opa = (start+end)//2
#             if num_list[opa]==x:
#                 print(opa+1)
#                 break
#             elif num_list[opa]<x:
#                 start=opa+1
#             else:
#                 end=opa-1
    


# import bisect

# shops = int(input())
# num_list = list(map(int, input().split()))
# num_list.sort()

# days = int(input())
# for _ in range(days):
#     x = int(input())
#     print(bisect.bisect_right(num_list, x))


shops=int(input())
num_list=list(map(int,input().split()))
num_list.sort()

# print(num_list)
days=int(input())
lst_index = [0] * days
day_list=[]
for i in range(days):
    x=int(input())

if num_list[0]>x:
    print(0)
elif num_list[-1]<=x:
    print(shops)
else:
    for j in range(shops):
        if num_list[j]>=x:
            print(j+1)
            break