#problem found at https://codeforces.com/problemset/problem/165/B/

import math
n,k = (int(_) for _ in input().split(' '))
temp = int(n-(n/k))
cur_low = 1
cur_high = n
m = n
while(m > 0):
    m = n
    temp2 = temp
    while(math.floor(temp2)>0):
        m -= int(temp2)
        temp2/=k
    if(m>0):
        temp+=1
print(temp)