input1 =int(input())
for i in range(input1):
    input2=input()
    resv=""
    resc=""
    
    for j in range(len(input2)):
        v=0
        if input2[j]=="a" or input2[j]=="e" or input2[j]=="i" or input2[j]=="o" or input2[j]=="u" :
           input2[v]+=resv[v]
        # else:
            
        v=v+1

    print(resv)
    print(resc)


    #print (f"Occurrence of '{input3}' in '{input2}' = {res}")        
    