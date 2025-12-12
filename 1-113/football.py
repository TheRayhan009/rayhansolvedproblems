num=input()
s=1
chak=False
for i in range(0,len(num)-1):
    if num[i] == num[i+1]:
        s=s+1
        if s > 6:
            print("YES")
            chak=True
            break
    else:
        chak=False
        s=1
if chak==False:
    print("NO")
