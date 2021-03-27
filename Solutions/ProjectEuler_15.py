size = 21
array = [[0 for i in range(size)] for j in range(size)]

for i in range(size):
    array[0][i] = 1
    array[i][0] = 1

for i in range(1,size):
    for j in range(1,size):
        array[i][j] = array[i-1][j] + array[i][j-1]

print(array[size-1][size-1])
