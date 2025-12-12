oparations=int(input())
for i in range(oparations):
    x=0
    apartment=input()
    if apartment[0]=="2":
        x=10*1
    elif apartment[0]=="3":
        x=10*2
    elif apartment[0]=="4":
        x=10*3
    elif apartment[0]=="5":
        x=10*4
    elif apartment[0]=="6":
        x=10*5
    elif apartment[0]=="7":
        x=10*6
    elif apartment[0]=="8":
        x=10*7
    elif apartment[0]=="9":
        x=10*8
    if len(apartment)==1:
        x=x+1
    if len(apartment)==2:
        x=x+2+1
    if len(apartment)==3:
        x=x+3+1+2
    if len(apartment)==4:
        x=x+4+3+2+1
    print(x)
