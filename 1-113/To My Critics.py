oparations=int(input())
for i in range(oparations):
    numbers=list(map(int,input().split()))
    x=min(numbers)
    numbers.remove(x)
    if numbers[0]+numbers[1]>9:
        print("YES")
    else:
        print("NO")