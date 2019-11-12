n = int(input())
i = 0
lst = list(map(int,input().split()))
x = max(lst)
for f in lst:
    if f == x:
        i+=1
print(i)