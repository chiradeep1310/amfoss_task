time = input().split(':')
x = time[2]
y = x[2:4]
z = x[0:2]
if y == 'pm':
    c = int(time[0]) + 12
    time[2] = z
    time[0] = c
else:
    time[2] = z
print(time)



