t=int(input())
for i in range (t):
    n=int(input())
    max_prime=0
    for j in range (1,n+1,2):
        if n%j==0:
            s=0
            for k in range (1,j+1):
                if j%k==0:
                    s+=1
            if s==2:
                if j>max_prime:
                    max_prime=j
    print(max_prime)
