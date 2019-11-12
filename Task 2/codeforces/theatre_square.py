n,m,a = list(map(int,input().split()))
if n%a==0:
    s1 = n/a
else:
    s1 = n//a + 1
if m%a == 0:
    s2 = m/a
else:
    s2 = m//a + 1
print(s1*s2)