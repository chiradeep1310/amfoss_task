n = int(input())
l = 0
for i in range(n):
    s = input()
    if s.rfind('+')!=-1:
        l+=1
    elif s.rfind('-')!=-1:
        l-=1
print(l)
