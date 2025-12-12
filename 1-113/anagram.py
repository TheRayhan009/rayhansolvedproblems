a=input()
b=input()
list_a=[]
list_b=[]
ans=0
for i in range(0,len(a)):
    list_a.append(a[i])
for i in range(0,len(b)):
    list_b.append(b[i])
for j in range(len(list_a)):
    if list_a[j] in list_b:
        list_b.remove(list_a[j])
        ans=ans+1
if ans==len(a):
    print("YES")
else:
    print("NO")
