import math
n = int(input())
l = list(map(int, input().split()))
texi = 0
ex = 0
for i in range(n):
    if l[i] == 4 or l[i] == 3:
        ex = ex + 1
    else:
        texi = texi + l[i]
output = math.ceil(texi/4) + ex
print(output)
