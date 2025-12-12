name=input()
up=0
down=0
for i in range(len(name)):
    if name[i]==name[i].upper():
        up=up+1
    else:
        down=down+1
s1=name.lower()
s2=name.upper()
if up==down:
    print(s1)
elif up>down:
    print(s2)
elif up<down:
    print(s1)

#ViP