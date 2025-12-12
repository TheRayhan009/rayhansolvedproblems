d l1=input()
l2 = ""
for i in range(len(l1)):
    if l1[i] not in l2:
        l2 =l2+l1[i]
x=len(l2)
if x % 2 !=0:
    print("IGNORE HIM!")

else:
    print("CHAT WITH HER!")