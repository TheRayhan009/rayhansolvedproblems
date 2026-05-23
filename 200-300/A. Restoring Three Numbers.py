# k,l,m,n=map(int,input().split())

# S_list=list(sorted([k,l,m,n]))

# print(S_list[-1]-S_list[0],S_list[-1]-S_list[1],S_list[-1]-S_list[2],sep=" ")


lengthx,l,m,n=map(int,input().split())
S_list=list(sorted([l,m,n]))
count = 1;

for i in range(lengthx):
    if lengthx-S_list[0] > S_list[1]:
        lengthx-=S_list[0]
        count+=1
    elif lengthx-S_list[1] > S_list[2]:
        lengthx-=S_list[1]
        count+=1
    else:
        count+=1
        break

print(count)