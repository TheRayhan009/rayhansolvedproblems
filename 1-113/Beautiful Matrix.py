matrix = []

for i in range(5):  # Assuming a 5x5 matrix based on your example
    row = list(map(int,input().split()))
    matrix.append(row)
# for  j in range(len(matrix)):
#     print(matrix.index('1'))

print(matrix[1][4])
