oparetion = int(input())
for i in range(oparetion):
    n=int(input())
    l=list(range(1,(n*2)+1))

    print(" ".join(map(str, l[n:])))