def main():
    n = int(input('the number and columns are '))
    arr = []
    for i in range(n):
        x = list(map(int,input().split()))
        arr.append(x)
    print(arr)
    print(array(arr,n))
def array(arr,n):
    sum1 = 0
    sum2 = 0
    for k in range(n):
        for j in range(n):
            if k == j:
                sum1+= arr[k][j]
            if k +j == n-1:
                sum2 += arr[k][j]
        print(sum1,sum2)
    if sum1>sum2:
        return (sum1-sum2)
    else:
        return(sum2-sum1)

main()