keybord=['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p','a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';','z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/']
lorr=input()
st=input()
ans=[]
if lorr=="R":
    for i in range(len(st)):
        index=keybord.index(st[i])
        a=index-1
        ans.append(keybord[a])
elif lorr=="L":
    for i in range(len(st)):
        index=keybord.index(st[i])
        a=index+1
        ans.append(keybord[a])
print(* ans,sep="")