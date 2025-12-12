n = int(input())
l=[]
for i in range(n):
    l.append(1)
for j in range(n-1):
    for i in range(1, n):
        l[i] += l[i - 1]
print(l[-1])