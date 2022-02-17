
from sympy import N


class Node:
    def __init__(self,left,right):
        self.rn = right
        self.ln = left

n = input()
inputs = []
visited = {}
query = []
q = []
count = 1

def dfs_check(a1,b1):
    a = int(a1.ln)
    b = int(a1.rn)
    c = int(b1.ln)
    d = int(b1.rn)
    acd = a>c and a<d
    bcd = b>c and b<d
    print("dfscheck" + "a = "+str(a) + "b = "+str(b) + "c= "+str(c)+ "d= "+str(d))
    print("a = "+ str(acd), "b = "+ str(bcd))
    print(bcd)
    if(acd or bcd):
        return True
    return False

def dfs(cur):
    q.append(cur)
    while(q):
        n = q.pop(0)
        visited[n] = 1
        for i in query:
            if not i in visited: 
                visited[i] = 1
                if dfs_check(n,i):
                    visited[n.rn] =2
                    q.append(i)

                   
for i in range(int(n)):
    inp = input()
    inputs.append(inp)

for i in range(int(n)):
    n_num = inputs[i].split(' ')
    list = [int(num_string) for num_string in n_num]
    n1 = list[0]
    n2 = list[1]
    n3 = list[2]
    visited = {}
    #print("n1" + str(n1))

    new_node = Node(n2,n3)
    if n1 == 1:
        query.append(new_node)
        #print("node = " + str(n2) + " " + str(n3))
    else:
        
        query.append(new_node)
        dfs(new_node)
        query.remove(new_node)
        if visited[n3] == 2:
            print("YES") 
        else: 
            print("NO")


