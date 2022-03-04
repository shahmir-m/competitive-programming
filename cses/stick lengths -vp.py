from array import array


n = int(input())
sticks = [int(length) for length in input().split()]
sticks.sort()
mid = sticks[int(n/2)]
cost = 0
for length in sticks:
	cost += abs(mid - length)

print(cost)