def palindrom(x):
    a = str(x)
    b = a[::-1]
    if a == b:
        return True
    else:
        return False
def factor(x):
    for k in range(100,1000):
        for j in range(100,1000):
            if j*k == x:
                return True
    else:
        return False
def main():
   t = int(input())
   k = 0
   for i in range(t):
       n = int(input())
       for i in range(n,0,-1):
           if palindrom(i) == True:
               if factor(i) == True:
                   print(i)
                   k+=1
                   break

main()

