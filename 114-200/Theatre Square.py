import math
x,y,a=map(int,input().split())

ans= 2*(x + y)

# x=math.ceil(x/a)
# y=math.ceil((y-a)*(x-a))
# y=math.ceil(y/a)


# if x/a is not isinstance and x != 1:
#     x=math.ceil(x/a)
# else:
#     x=x//a
# # x=math.ceil(x/a)
# if x/a is not isinstance and y != 1:
#     y=math.ceil(y/a)
# elif y == 1:
#     y=y//a

print(ans//(4*a))