# l=input()
# count=[]
# ans=0
# x=1
# index=0
# for i in range(0,len(l),2):
#     for j in range(x):
#         if l[j] == count[i]:
#             ans =+ 1
#         else:
#             count.append(l[i])
#         x=+1
#         # print(count)
# print(ans)


l=input()
count=""
count = count + l[0]
ans=0
x=1
index=0
for i in range(2,len(l),2):
    for j in range(x*2):
        if l[i] in count[j]:
            ans =+ 1
        elif l[i] not in count[j] and l[i]!=" ":
            count = " " + count + l[i]
        x=+1
        # print(count)
print(ans)