def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        lst = fib(n)
def fib(n):
    fib_list = []
    sum = 0
    a = 1
    b = 2
    for i in range(3,n//2+1):
        c = a+b
        fib_list.append(c)
        a = b
        b = c
main()