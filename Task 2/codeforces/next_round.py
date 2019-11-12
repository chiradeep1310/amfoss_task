t,k = input().split(' ')
l = 0
lst = list(map(int,input().split()))
k1 = lst[int(k)-1]
for a in lst:
    if k1 == 0 & a ==k1:
        l+=0
    elif k1 <= a:
        l += 1
    else:
        l+=0
print(l)