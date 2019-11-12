def main():
    a = list(map(int,input('please give the scores of alice').split()))
    b = list(map(int,input('please give the scores of bob').split()))
    print(score_of_contestents(a,b))

def score_of_contestents(a,b):
    s1 = 0
    s2 = 0
    j = 0
    n = 1
    for i in range(len(a)):
            if a[i] > b[j]:
                s1 = s1 + 1
            if b[j] > a[i]:
                s2 = s2 + 1
            j = j + 1
    return (s1 , s2)
main()