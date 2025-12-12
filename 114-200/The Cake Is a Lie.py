oparetion=int(input())
for i in range(oparetion):
    x,y,k=map(int,input().split())
    a=1  #You are standing at cell (1[a],1[b]) in primary
    b=1  #You are standing at cell (1[a],1[b]) in primary
    x_chak=True # for check only x point .
    y_chak=False # for check only y point . but for now its False.
    ans=0 # its store burles.
    for j in range(x+y):
        if a==x and b==y:
            break # for exit the loop.
        if x_chak==True:
            if a<x:
                a+=1
                ans+=b
            else:
                x_chak=False # now its False.
                y_chak=True # its now True.
        if y_chak==True: # now check this ..
            if b<y:
                b+=1
                ans+=a
    if ans==k: 
        print("YES")
    else:
        print("NO")
        
#i hope you understand!!!!