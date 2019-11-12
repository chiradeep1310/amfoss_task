n = int(input())
for i in  range (n):
    s = input()
    if len(s)>10:
        s1 = s[0]
        s2 = s[len(s)-1]
        s3 = len(s) - 2
        print(s1+str(s3)+s2)
    else:
        print(s)
