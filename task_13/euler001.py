def cal(x):
    return((x*(x+1))//2)
def main():
    t=int(input())
    for i in range (t):
        n=int(input())
        n-=1
        x=n//3
        y=n//5
        z=n//15
        print((3*cal(x))+(5*cal(y))-(15*cal(z)))
