import math
bank_money=int(input())
ans=0
if bank_money >= 100:
    x=math.floor(bank_money/100)
    ans+=x
    bank_money=bank_money - x*100
    
if bank_money >= 20:
    x=math.floor(bank_money/20)
    ans+=x
    bank_money=bank_money - x*20
    
if bank_money >= 10:
    x=math.floor(bank_money/10)
    ans+=x
    bank_money=bank_money - x*10
    
if bank_money >= 5:
    x=math.floor(bank_money/5)
    ans+=x
    bank_money=bank_money - x*5
    
if bank_money >= 1:
    x=math.floor(bank_money/1)
    ans+=x
    bank_money=bank_money - x*1
    
print(ans)
