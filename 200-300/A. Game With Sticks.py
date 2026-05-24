k,l=map(int,input().split())
if k==l:
    if k%2==0:
        print("Malvika")
    else:
        print("Akshat")
elif k<l:
    if k%2==0:
        print("Malvika")
    else:
        print("Akshat")
else:
    if l%2==0:
        print("Malvika")
    else:
        print("Akshat")