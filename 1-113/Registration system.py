cases=int(input())
storag=[]
for i in range(cases):
    inputs=input()
    x=storag.count(inputs)
    if inputs not in storag:
        storag.append(inputs)
        #print(storag)
        print("OK")
    else:
        storag.append(inputs)
        print(*inputs,x,sep="")
    storag.sort()