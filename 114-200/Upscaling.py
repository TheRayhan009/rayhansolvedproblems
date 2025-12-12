oparetions=int(input())
for i in range(oparetions):
    num_of_boxes=int(input())
    dot_chak=False
    dot=False
    for j in range(0,num_of_boxes):
        if j%2==0:
            dot_chak=False
        elif j%2!=0:
            dot_chak=True
        if dot_chak==True:
            for z in range(2):
                dot=False
                for x in range(num_of_boxes):
                    if dot==True:
                        dot=False
                        print("##",end="")
                    else:
                        dot=True
                        print("..",end="")
            
                print("")
            dot=True
        elif dot_chak==False:
            for z in range(2):
                dot=False
                for x in range(num_of_boxes):
                    if dot==False:
                        dot=True
                        print("##",end="")
                    else:
                        dot=False
                        print("..",end="")
                    
                print("")
            