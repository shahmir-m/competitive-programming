from audioop import reverse


n,m = (int(i) for i in input().split(' '))
dist = [0 for _ in range(n+1)]
edges = [0 for _ in range(m)]
relax = [-1 for _ in range(n+1)] 

def bmf():
    for i in range(n):
        x = -1
        for e in edges:
            a,b,c = e
            if(dist[a]+c < dist[b]):
                dist[b] = dist[a]+c
                x = b
                relax[b] = a
    if x == -1:
        print("NO")
    else:
        for _ in range(n+1):
            x = relax[x]
        cycle = list()
        v = x
        while(1):
            cycle.append(v)
            if (v==x) and (len(cycle) > 1):
                break
            v = relax[v]

        cycle.reverse()
        print("YES")
        for c in cycle:
            print(c,end=" ")
for i in range(m):
    a,b,c = (int(j) for j in input().split(' '))
    edges[i] = [a,b,c]
bmf()