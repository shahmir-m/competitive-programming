str_input = input()
str_list = str_input.split(' ')
#working backwards
list = [int(num_string) for num_string in str_list]
start = list[0]
target = list[1]


num_clicks = 0
while(target != start):
    if(target < start):
        target += 1
    elif(target %2 == 0):
        target /= 2            
    else:
        target += 1
    num_clicks+= 1

print(num_clicks)
