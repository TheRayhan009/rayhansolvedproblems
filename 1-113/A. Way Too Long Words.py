line = int(input())

for i in range(line):
    word = input()
    x = len(word)
    if x <11:
        print (word)

    else :
        print(word[0],end="")
        print(x - 2,end="")
        print(word[x - 1])
