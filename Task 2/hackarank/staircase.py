n = int(input())
for i in range(1,n+1):
    space = n -i
    for s in range(space):
        print(' ',end = '')
    hash = n - space
    for j in range(hash):
        print('#',end='')
    print('')