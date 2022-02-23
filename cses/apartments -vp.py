
# problem found at https://cses.fi/problemset/task/1084/
n, m, t = map(int, input().split())
list = input().split(' ')
app = [int(num_string) for num_string in list]
app.sort()
list = input().split(' ')
apt = [int(num_string) for num_string in list]
apt.sort()


app_counter = 0
apt_counter = 0  
ret = 0
while app_counter < n and apt_counter < m:
	cur_app = app[app_counter]
	cur_apt = apt[apt_counter]
	if cur_apt < cur_app - t:
		apt_counter += 1
	elif cur_apt > cur_app + t:
		app_counter += 1
	else:
		ret += 1
		app_counter += 1
		apt_counter += 1
print(ret)