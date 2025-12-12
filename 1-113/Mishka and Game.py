games=int(input())
m=0
c=0
for i in range(games):
    mishka,chris=map(int,input().split())
    if mishka>chris:
        m=m+1
    elif mishka<chris:
        c=c+1
if m>c:
    print("Mishka")
elif m<c:
    print("Chris")
elif m==c:
    print("Friendship is magic!^^")