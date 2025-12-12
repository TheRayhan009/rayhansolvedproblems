banabas,dolars,buying_bananas=map(int,input().split())
# dolars=map(int,input().split)
# buying_bananas=map(int,input().split)
nees_dolar=0
ans=0
l1=buying_bananas+1
for j in range(1,l1):
    nees_dolar=banabas*j
    ans=ans+nees_dolar
    nees_dolar=0
if ans- dolars<= -1:
    print("0")
    
else :
   print(ans-dolars)
    
# banabas=banabas+1
