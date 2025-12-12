input1 =int (input())
for i in range(input1):
    input2=input()
    input3=input()
    res=0;
    for j in range(len(input2)):
        if input2[j]==input3:
            res=res+1
    
    print (f"Occurrence of '{input3}' in '{input2}' = {res}")        
    