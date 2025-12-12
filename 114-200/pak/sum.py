def sum(a,b):
    print(a+b)
def mal(a,b):
    print(a-b)
def sq(a):
    print(a*a)
def nxd(a,b,l):
    x=b-1
    n=l[x]
    count=0
    for i in range(a):
        if int(l[i])>=int(n) and l[i]!="0":
            count=count+1
    print(count)
def calculator(a,sine,b):

    if sine=="+":
        print("Ans ->",a+b)
    elif sine=="-":
        print("Ans ->",a-b)
    elif sine=="x":
        print("Ans ->",a*b)
    elif sine=="/":
        print("Ans ->",a/b)
    elif sine=="^":
        print("Ans ->",a**b)
    elif sine=="%":
        print("Ans ->",a%b)
