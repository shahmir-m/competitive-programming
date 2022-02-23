cur_num = int(input())

matrix = []
matrix.append(cur_num)

while(cur_num != 1):
    if cur_num % 2 == 1:
        cur_num = cur_num*3 + 1
    else:
        cur_num = int(cur_num/2)
    matrix.append(cur_num)

print(*matrix)

