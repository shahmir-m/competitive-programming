
from collections import deque
import sys

# get the input dimensions and labyrinth
dimensions = input().split(' ')
list = [int(num_string) for num_string in dimensions]
row = list[0]
col = list[1]
lab = [[]]
row_c = 0
for i in range(row):
    input_row = input()
    for j in range(len(input_row)):
        if input_row[j] == 'A':
            start_r = row_c
            start_c = j
    lab.insert(i,input_row)
    row_c+=1

#locate the start and end of the lab

found = False
#init BFS
dir_r = [-1, 0, 1, 0]
dir_c = [0, -1, 0, 1]
dir_s = "ULDR"
visited = {}
sol = {}
queue = []
path = []
queue.append((start_r,start_c))
visited[tuple([start_r,start_c])] = True

def is_valid(r,c):
    if(r >= 0 and r < row and c >= 0 and c < col):
        if(lab[r][c]!='#' and not tuple([r,c]) in visited):
            return True
    return False

while(queue):
    cur_r,cur_c = queue.pop(0)
    if lab[cur_r][cur_c] == 'B':
        #work backwards from directional array to get the correct path
        while not found:
            path.append(sol[cur_r,cur_c])
            if(path[-1] == 'L'):
                cur_c+=1
            if(path[-1] == 'R'):
                cur_c-=1
            if(path[-1] == 'U'):
                cur_r+=1
            if(path[-1] == 'D'):
                cur_r-=1
            if(cur_c == start_c and cur_r == start_r):
                found = True
                break
        break
    for dir in range(4):
        r = cur_r + dir_r[dir]
        c = cur_c + dir_c[dir]
        if is_valid(r,c):
            sol[tuple([r,c])] = dir_s[dir]
            queue.append((r,c))
            visited[tuple([r,c])] = True


if len(path) > 0:
    print("YES")
    print(len(path))
    path.reverse()
    for i in path:
        print(i,end="")
    print("")
else:
    print("NO")