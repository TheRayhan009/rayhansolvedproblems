user_st=str(input())
x=0
ans_st=""
chak=False
while x<len(user_st):
    if user_st[x:x+3]!="WUB":
        ans_st+=user_st[x]
        x+=1
        chak=True
    else:
        if chak==True:
            chak=False
            ans_st+=" "
        x+=3
print(ans_st)