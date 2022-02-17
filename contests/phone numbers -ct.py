n = input()
should = []

def sum_digits(string):
    sum = 0
    num = int(string)
    while(num > 0):
        sum += int(num%10)
        num = int(num/10)
    return True if sum%2==0 else False

for i in range(int(n)):
    row = input().split(' ')
    if sum_digits(row[1]):
        should.append(row[0])

for i in should:
    print(i)

