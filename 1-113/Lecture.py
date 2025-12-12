sentence,wordes=map(int,input().split())
list_wordes=[]
list_wordes1=[]
list_wordes2=[]
ans=""
for j in range(wordes):
    s1,s2=map(str,input().split())
    list_wordes1.append(s1)
    list_wordes2.append(s2)
list_line=list(map(str,input().split()))
for k in range(sentence):
    if list_line[k] in list_wordes1:
        x=list_wordes1.index(list_line[k])
        if len(list_line[k])==len(list_wordes2[x]):
            list_wordes.append(list_wordes1[x])
        elif len(list_line[k])>len(list_wordes2[x]):
            list_wordes.append(list_wordes2[x])
        elif len(list_line[k])<len(list_wordes2[x]):
            list_wordes.append(list_line[k])
    elif list_line[k] in list_wordes2:
        x=list_wordes2.index(list_line[k])
        if len(list_line[k])==len(list_wordes1[x]):
            list_wordes.append(list_wordes1[x])
        elif len(list_line[k])>len(list_wordes1[x]):
            list_wordes.append(list_wordes1[x])
        elif len(list_line[k])<len(list_wordes1[x]):
            list_wordes.append(list_line[k])
print(*list_wordes,sep=" ")

#  level : 1000

'''
if len(s1)==len(s2):
        list_wordes.append(s1)
    elif s1>s2:
        list_wordes.append(s2)
    elif s1<s2:
        list_wordes.append(s1)

'''