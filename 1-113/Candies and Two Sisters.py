#my program
# problem : Time limit exceeded
# distributeing_case=int(input())
# w=1
# for i in range(distributeing_case):
#     ans=0
#     Candies=int(input())
#     a=Candies-1
#     b=1
#     if Candies>2:
#         w=0
#         for j in range(Candies):
#             if a+b < Candies:
#                 break
#             elif a>b:
#                 ans = ans +1
#             a = a - 1
#             b = b + 1
#     elif w==1:
#         print("0")
#     else:
#         print(ans)

distributeing_case=int(input())
for i in range(distributeing_case):
    ans=0
    Candies=int(input())
    if Candies>2:
        ans = int((Candies-1)/2)
        print(ans)
    else:
        print("0")