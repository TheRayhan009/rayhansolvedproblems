oparetion=int(input())
cop=[]
l=[]
for i in range(oparetion):
    st=input()    
    if st not in cop:
        cop.append(st)
        l.append(st+"1")
        print("OK")
    else:
        qq=cop.index(st)
        a=""
        m=""
        w=0
        q=0
        for o in range(len(l[qq])-1,-1,-1):
            if l[qq][o].isdigit():
                a = l[qq][o] + a
                w = w + 1
            else:
                break
        m = l[qq][0:len(l[qq])-w]
        # print(type(l[j][q]), l[j][q])
        # print(len(l[j][q]), w)

        # print(m)
        if m==st:
            #print(a)
            print(*m,int(a),sep="")
            l[qq]=m+str(int(a)+1)
            # print(l)
                