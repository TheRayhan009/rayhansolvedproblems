first_strength_of_Kirito,cases=map(int,input().split())
x=0
y=0
ans=first_strength_of_Kirito
for i in range(cases):
    dragons_strength,Kirito_strength=map(int,input().split())
    if ans>dragons_strength:
        Kirito_strength = Kirito_strength + first_strength_of_Kirito
        ans = Kirito_strength + dragons_strength
        x = x + 1
    else:
        ans = Kirito_strength + dragons_strength
if ans>=x:
    print("YES")
else:
    print("NO")