l=input()
x=0
for i in range(len(l)):
    if l[i] in "H" or l[i] in "Q" or l[i] in "9":
        print("YES")
        x=1
        break
if x==0:
    print("NO")