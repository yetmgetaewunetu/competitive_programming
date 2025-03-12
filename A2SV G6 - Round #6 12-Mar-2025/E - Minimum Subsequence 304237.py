# Problem: E - Minimum Subsequence - https://codeforces.com/gym/594077/problem/E

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,list(input())))
    zeros = []
    ones = []
    num = 1
    res = 0
    for i in range(n):
        if arr[i] == 0:
            if ones:
                arr[i] = ones[-1]
                ones.pop()
                zeros.append(arr[i])
            else:
                arr[i] = num
                zeros.append(num)
                res = num
                num += 1
        else:
            if zeros:
                arr[i] = zeros[-1]
                zeros.pop()
                ones.append(arr[i])
            else:
                arr[i] = num
                ones.append(num)
                res = num
                num += 1
    print(res)
    print(*arr)



