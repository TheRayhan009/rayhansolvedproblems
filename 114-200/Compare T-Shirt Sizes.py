oparetion=int(input())
for i in range(oparetion):
    a,b=map(str,input().split())
    list_a=list(a)
    list_b=list(b)
    x=0
    y=0
    if list_a[-1]=="S" and list_b[-1]=="S":
        x=list_a.count("X")
        y=list_b.count("X")
        if x==y:
            print("=")
        elif x>y:
            print("<")
        elif x<y:
            print(">")
    elif list_a[-1]=="M" and list_b[-1]=="M":
        x=list_a.count("X")
        y=list_b.count("X")
        if x==y:
            print("=")
        elif x>y:
            print(">")
        elif x<y:
            print("<")
    elif list_a[-1]=="L" and list_b[-1]=="L":
        x=list_a.count("X")
        y=list_b.count("X")
        if x==y:
            print("=")
        elif x>y:
            print(">")
        elif x<y:
            print("<")
    elif list_a[-1]=="S" and list_b[-1]=="M":
        print("<")
    elif list_a[-1]=="S" and list_b[-1]=="L":
        print("<")
    elif list_a[-1]=="M" and list_b[-1]=="S":
        print(">")
    elif list_a[-1]=="L" and list_b[-1]=="S":
        print(">")
    elif list_a[-1]=="M" and list_b[-1]=="L":
        print("<")
    elif list_a[-1]=="L" and list_b[-1]=="M":
        print(">")