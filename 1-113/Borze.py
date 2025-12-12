borze_code = input()
ans = ""

i = 0
while i < len(borze_code):
    if borze_code[i] == '.':
        ans += '0'
        i += 1
    elif borze_code[i] == '-' and borze_code[i + 1] == '.':
        ans += '1'
        i += 2
    elif borze_code[i] == '-' and borze_code[i + 1] == '-':
        ans += '2'
        i += 2

print(ans)
