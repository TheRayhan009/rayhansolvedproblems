n=int(input())
for i in range(n):
    a=int(input())
    l=list(map(int,input().split()))
    
    Mihai_candies=0
    Bianca_candies=0
    
    for j in l:
        if j%2==0:
            Mihai_candies+=j
        else:
            Bianca_candies+=j
    
    if Mihai_candies>Bianca_candies:
        print("YES")
    else:
        print("NO")