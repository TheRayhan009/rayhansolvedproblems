import math
opa=int(input())
for i in range(opa):
    lenx=int(input())
    numbers = list(map(int, input().split()))  # Read space-separated numbers  
    sumx = sum(numbers)  # Compute sum  

        
    if math.sqrt(sumx) == int(math.sqrt(sumx)):  
        print("YES")  
    else:  
        print("NO")  