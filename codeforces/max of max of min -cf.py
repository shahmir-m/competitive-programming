
#problem can be found at https://codeforces.com/contest/870/problem/B/

n,k = (int(_) for _ in input().split(' '))
arr = [int(num_string) for num_string in input().split()]


if k == 1:
    print(min(arr))
elif k >= 3:
    print(max(arr))
else:
    left = [arr[0]] * len(arr)
    right = [arr[len(arr)-1]] * len(arr)
    answer = float('-inf')
    for i in range(1, len(arr)):
        left[i] = min(left[i-1], arr[i])
 
    for i in range(len(arr)-2, -1, -1):
        right[i] = min(right[i+1], arr[i])
 
    for i in range(len(arr)-1):
        answer = max(answer, max(left[i], right[i-1]))
 
    print(answer)