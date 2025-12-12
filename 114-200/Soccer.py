o=int(input())
for i in range(o):
    a,b=map(int,(input().split()))
    c,d=map(int,(input().split()))
    if a<d and d>c:
        print("YES")
    else:
        print("NO")