oparetion=int(input())
for i in range(oparetion):
    a,b,c,d=map(int,input().split())
    # a.sort()
    x_chak=False
    y_chak=False
    if min(a,b)<min(c,d):
        for i in range(min(a,b),max(a,b)):
            if i==min(c,d):
                x_chak=True
            elif i==max(c,d):
                y_chak=True
        if x_chak==True and y_chak==False:
            print("YES")
        else:
            print("NO")
             
    elif min(a,b)>min(c,d):
        for i in range(min(c,d),max(c,d)):
            if i==min(a,b):
                x_chak=True
            elif i==max(a,b):
                y_chak=True
        if x_chak==True and y_chak==False:
            print("YES")
        else:
            print("NO")