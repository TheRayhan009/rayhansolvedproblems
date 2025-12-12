oparations=int(input())
for i in range(oparations):
    ans=""
    l1=input()
    l2=input()
    l3=input()
    l4=input()
    l5=input()
    l6=input()
    l7=input()
    l8=input()
    for j in range(len(l1)):
        if l1[j]!=".":
            ans=ans+l1[j]
    for j in range(len(l2)):
        if l2[j]!=".":
            ans=ans+l2[j]
    for j in range(len(l3)):
        if l3[j]!=".":
            ans=ans+l3[j]
    for j in range(len(l4)):
        if l4[j]!=".":
            ans=ans+l4[j]
    for j in range(len(l5)):
        if l5[j]!=".":
            ans=ans+l5[j]
    for j in range(len(l6)):
        if l6[j]!=".":
            ans=ans+l6[j]
    for j in range(len(l7)):
        if l7[j]!=".":
            ans=ans+l7[j]
    for j in range(len(l8)):
        if l8[j]!=".":
            ans=ans+l8[j]
    print(ans)