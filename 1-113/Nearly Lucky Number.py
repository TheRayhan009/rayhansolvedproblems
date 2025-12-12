line = int(input())
ls=str(line)
lacy=0
unlacy=0
for i in range(0,len(ls)):
    if ls[i] == '4' or ls[i] == '7':
        lacy=lacy+1
    else:
        unlacy=unlacy+1
if lacy==7 or lacy==4:
    print("YES")
else:
    print("NO")