# problem : TIME_LIMIT_EXCEEDED
import math
money = int(input())
x = money
receipt = 0
a=int(math.sqrt(money))
y=0
if money%100==0:
    q=int(money/100)
    receipt=receipt+q
else:
    while a>y:
        if x >= 100:
            x -= 100
            receipt += 1
        elif x >= 20:
            x -= 20
            receipt += 1
        elif x >= 10:
            x -= 10
            receipt += 1
        elif x >= 5:
            x -= 5
            receipt += 1
        elif x >= 1:
            x -= 1
            receipt += 1
        else:
            break
        a=a+1
print(receipt)