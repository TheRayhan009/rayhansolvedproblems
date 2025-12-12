import math
q,w,a=map(int,input().split())

x=math.ceil(q/a)
y=math.ceil(w/a)

print(x*y)