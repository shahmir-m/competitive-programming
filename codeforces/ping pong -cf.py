
#problem can be found at https://codeforces.com/problemset/problem/320/B/

from collections import deque
class Node:
    def __init__(self,left,right):
        self.rn = right
        self.ln = left

n = input()
inputs = []
visited = []
query = []
q = []
count = 0

def dfs_check(a1,b1):
    a = int(a1.ln)
    b = int(a1.rn)
    c = int(b1.ln)
    d = int(b1.rn)
    #print("dfscheck " + "a = "+str(a) + " b = "+str(b) + " c= "+str(c)+ " d= "+str(d))
    #print("a = "+ str(acd), "b = "+ str(bcd))
    if c < a < d or c < b < d:
        return True
    return False

def dfs(cur):
    q = deque([cur.ln-1])
    visited = [False] * len(query)
    visited[cur.ln-1] = True
    while(q):
        n = q.pop()
        node = query[n]
        for i in range(len(query)):
            if not visited[i]:
                if dfs_check(node,query[i]):   
                    q.append(i)
                    visited[i] = True
    return visited[cur.rn-1]

                   
for i in range(int(n)):
    inp = input()
    inputs.append(inp)

for i in range(int(n)):
    n_num = inputs[i].split(' ')
    list = [int(num_string) for num_string in n_num]
    n1 = list[0]
    n2 = list[1]
    n3 = list[2]
    #print("n1" + str(n1))
    new_node = Node(n2,n3)
    if n1 == 1:
        query.append(new_node)
    else:
        ans = dfs(new_node)
        if not ans:
            print("NO") 
        else: 
            print("YES")


