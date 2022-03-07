n,m = (int(i) for i in input().split(' '))
trees = list()
class pair:
    def __init__(self,num,beauty):
        self.n = num
        self.b = beauty

    def __repr__(self):
        return str((self.n,self.b))
for _ in range(n):
    list = [int(s) for s in input().split()]
    trees.append(pair(list[0],list[1]))
trees.sort(key=lambda x: x.b)
trees.reverse()

taken = 0 
bp = 0
for i in range(n):
    k = 0
    while(taken < m and k<trees[i].n):
        taken+=1
        bp+=trees[i].b
        k+=1

print(bp)
