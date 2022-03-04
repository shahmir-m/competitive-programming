#problem can be found at https://codeforces.com/problemset/problem/405/A/

num_col = input()
str_input = input()

str_list = str_input.split(' ')
list = [int(num_string) for num_string in str_list]
list.sort()

print(*list)

    