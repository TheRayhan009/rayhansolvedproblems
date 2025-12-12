oparations=int(input())
for i in range(oparations):
    player_strent=list(map(int,input().split()))
    ans=[]
    if player_strent[0]>player_strent[1]:
        ans.append(player_strent[0])
    if player_strent[0]<player_strent[1]:
        ans.append(player_strent[1])
    if player_strent[2]<player_strent[3]:
        ans.append(player_strent[3])
    if player_strent[2]>player_strent[3]:
        ans.append(player_strent[2])
    player_strent.sort(reverse=True)
    if player_strent[0]==ans[0] and player_strent[1]==ans[1] or player_strent[0]==ans[1] and player_strent[1]==ans[0]:
        print("YES")
    else:
        print("NO")
        







    # player_strent.sort(reverse=True)
    # print(player_strent)
    # if player_strent[0] == ans[0] and player_strent[1] in ans[1] or player_strent[0] == ans[1] and player_strent[1] in ans[0]:
    #     print("YES")
    # else:
    #     print("NO")