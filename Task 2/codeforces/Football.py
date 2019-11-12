n = input()
l = 0
k = 0
lst = list(n)
for i in range(len(lst)-1):
    if lst[i]==lst[i+1]:
        l+=1
    if l==6:
        k+=1
        print('yes')
        break
if k==0:
    print('no')