oparations=int(input())
for i in range(oparations):
    input_len=int(input())
    st=input()
    front_Bracket=0
    back_Bracket=0
    breaks=0
    for j in range(input_len):
        if st[j]=="(":
            front_Bracket=front_Bracket+1
        elif st[j]==")" and front_Bracket<=0:
            breaks=breaks+1
        else:
            front_Bracket=front_Bracket-1
    print(breaks)
#level : 1000