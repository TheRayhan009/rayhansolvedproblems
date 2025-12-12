ls =int(input())
l=input()
a=0
d=0
for i in range(ls):
    if l[i]=="A":
        a=a+1
    else:
        d=d+1
if a==d:
    print("Friendship")
elif a>d:
    print("Anton")
else:
    print("Danik")