# k,l,m,n=map(int,input().split())

# S_list=list(sorted([k,l,m,n]))

# print(S_list[-1]-S_list[0],S_list[-1]-S_list[1],S_list[-1]-S_list[2],sep=" ")


oparetion = int(input())
for i in range(oparetion):
    n=int(input())
    l=list(range(1,(n*2)+1))

    print(" ".join(map(str, l[n:])))

    # for j in range(n-1):
    #     l.append(l[j]+l[j+1])
    # setx=set(l)
    # setx=list(setx)
    # print(setx,sep=" ")

    