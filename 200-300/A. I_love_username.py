oparetion=input()
l = list(map(int, input().split()))
# print(l)
minx=maxx=l[0]
nice=0
for i in range(len(l)):
    if l[i] < minx:
        nice+=1
        minx=l[i]
    elif l[i] > maxx:
        nice+=1
        maxx=l[i]

print(nice)