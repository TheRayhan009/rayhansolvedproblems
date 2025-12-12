import math
num,num_index=map(int,input().split())
if math.ceil(num/2) < num_index:
    even_index=num_index-math.ceil(num/2)
    print(2*even_index)
else:
    print((2*num_index)-1)