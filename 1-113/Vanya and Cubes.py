cubs=int(input())
conten=0
lear=0
for i in range(1,cubs+1):
    conten=conten+i
    if cubs>=conten:
        cubs=cubs-conten
        lear=lear+1
    else:
        break

print(lear)