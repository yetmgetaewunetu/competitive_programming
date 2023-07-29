t = int(input())
for i in range(t):
    n = int(input())
    N = list(map(int, input().split()))
    N.sort()
    flag = 'YES'
    for i in range(1 , n):
        if N[i] - N[i -1]>1:
            flag = 'NO'
            break
    print(flag)
