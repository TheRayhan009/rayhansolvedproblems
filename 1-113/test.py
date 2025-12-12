# a,b,x,c,d=map(int,input().split())
# if a<=c and c<=d:
#     len_mat=a*b
#     len_room=c*d*x
#     print(int(len_room/len_mat))
# else:
#     print("0")

# oparations=int(input())
# for i in range(oparations):
#     line=int(input())
#     a=list(map(int,input().split()))
#     a.sort(reverse=True)
#     x=0
#     cars_price=0
#     for j in range(len(a)):
#         if a[j]!=0:
#             cars_price=cars_price+(a[j]-x)
#         x=x+1
#     cars_price=cars_price%1000000007
#     print(cars_price)
l=[4, 3, 1, 2, 7, 8, 7, 9, 4, 2]
print(l[-2])
