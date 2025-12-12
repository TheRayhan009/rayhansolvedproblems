l=int(input())
room=0
for i in range(l):
    a,b=map(int,input().split())
    x=b-2
    if a==0 and b>=2:
        room += 1
    elif a<=x:
        room += 1
    
print(room)
