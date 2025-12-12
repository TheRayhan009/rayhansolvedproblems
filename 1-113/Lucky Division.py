l=input()
x=0
if "4" in l and "7" in l and "1" not in l and "2" not in l and "3" not in l and "5" not in l and "6" not in l and "8" not in l and "9" not in l and "0" not in l :
    print("YES")
    x=1
else:
    l=int(l)
    if l%4==0 or l%7==0:
        x=1
        print("YES")
    else:
        l=int(l)
        for i in range(l):
            i=str(i)
            if "4" in i and "7" in i and "1" not in i and "2" not in i and "3" not in i and "5" not in i and "6" not in i and "8" not in i and "9" not in i and "0" not in i :
                i=int(i)
                if l%i==0:
                    print("YES")
                    x=1
                    break
            i=int(i)
    if x==0:
        print("NO")
        