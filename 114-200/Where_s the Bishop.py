import math
oparetion=int(input())
for i in range(oparetion):
    ans1=""
    ans2=0
    position_1_input=input()
    position_2_input=input()
    position_3_input=input()
    position_4_input=input()
    position_5_input=input()
    position_6_input=input()
    position_7_input=input()
    position_8_input=input()
    #...................................................
    position_1=list(position_1_input)
    position_2=list(position_2_input)
    position_3=list(position_3_input)
    position_4=list(position_4_input)
    position_5=list(position_5_input)
    position_6=list(position_6_input)
    position_7=list(position_7_input)
    position_8=list(position_8_input)

    has_lenx1=position_1.count("#")
    has_lenx2=position_2.count("#")
    has_lenx3=position_3.count("#")
    has_lenx4=position_4.count("#")
    has_lenx5=position_5.count("#")
    has_lenx6=position_6.count("#")
    has_lenx7=position_7.count("#")
    has_lenx8=position_8.count("#")
    
    if has_lenx1 == 1 and has_lenx2 == 2:
        ans1 = "1"
        ans2 = position_1.index("#") + 1
    elif has_lenx2 == 1 and has_lenx3 == 2 or has_lenx1 == 2:
        ans1 = "2"
        ans2 = position_2.index("#") + 1
    elif has_lenx3 == 1 and has_lenx4 == 2 or has_lenx2 == 2:
        ans1 = "3"
        ans2 = position_3.index("#") + 1
    elif has_lenx4 == 1 and has_lenx5 == 2 or has_lenx3 == 2:
        ans1 = "4"
        ans2 = position_4.index("#") + 1
    elif has_lenx5 == 1 and has_lenx6 == 2 or has_lenx4 == 2:
        ans1 = "5"
        ans2 = position_5.index("#") + 1
    elif has_lenx6 == 1 and has_lenx7 == 2 or has_lenx5 == 2:
        ans1 = "6"
        ans2 = position_6.index("#") + 1
    elif has_lenx7 == 1 and has_lenx8 == 2 or has_lenx6 == 2:
        ans1 = "7"
        ans2 = position_7.index("#") + 1
    elif has_lenx8 == 1 and has_lenx7 == 2:
        ans1 = "8"
        ans2 = position_8.index("#") + 1
    
    print(ans1,ans2)