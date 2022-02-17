
n = input()
lim = int(input())
chocs_str = input().split(' ')
chocs = []
for n in chocs_str:
    chocs.append(int(n))
sum = 0
for c in chocs:
    if(lim - c > 0):
        sum+=1
        lim-=c
    else:
        print(sum)
        break


