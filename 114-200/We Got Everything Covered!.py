oparetion=int(input())
for i in range(oparetion):
    y,x=map(int,input().split())
    # y+=1
    ans=""
    for j in range(y): 
        if x==1:
            for j in range(y):
                ans+="a"
            x-=1
        elif x==2:
            for j in range(y):
                ans+="b"
            x-=1
        elif x==3:
            for j in range(y):
                ans+="c"
            x-=1
        elif x==4:
            for j in range(y):
                ans+="d"
            x-=1
        elif x==5:
            for j in range(y):
                ans+="e"
            x-=1
        elif x==6:
            for j in range(y):
                ans+="f"
            x-=1
        elif x==7:
            for j in range(y):
                ans+="g"
            x-=1
        elif x==8:
            for j in range(y):
                ans+="h"
            x-=1
        elif x==9:
            for j in range(y):
                ans+="i"
            x-=1
        elif x==10:
            for j in range(y):
                ans+="j"
            x-=1
        elif x==11:
            for j in range(y):
                ans+="k"
            x-=1
        elif x==12:
            for j in range(y):
                ans+="l"
            x-=1
        elif x==13:
            for j in range(y):
                ans+="m"
            x-=1
        elif x==14:
            for j in range(y):
                ans+="n"
            x-=1
        elif x==15:
            for j in range(y):
                ans+="o"
            x-=1
        elif x==16:
            for j in range(y):
                ans+="p"
            x-=1
        elif x==17:
            for j in range(y):
                ans+="q"
            x-=1
        elif x==18:
            for j in range(y):
                ans+="r"
            x-=1
        elif x==19:
            for j in range(y):
                ans+="s"
            x-=1
        elif x==20:
            for j in range(y):
                ans+="t"
            x-=1
        elif x==21:
            for j in range(y):
                ans+="u"
            x-=1
        elif x==22:
            for j in range(y):
                ans+="v"
            x-=1
        elif x==23:
            for j in range(y):
                ans+="w"
            x-=1
        elif x==24:
            for j in range(y):
                ans+="x"
            x-=1
        elif x==25:
            for j in range(y):
                ans+="x"
            x-=1
        elif x==26:
            for j in range(y):
                ans+="z"
            x-=1
    print(ans)