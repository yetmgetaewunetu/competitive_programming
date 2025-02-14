# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    i,j = 0,0
    res = 0
    flag = True
    while j < n:
        if arr[j] >0:
            cur = arr[j]
            while j < n and arr[j] >0:
                cur = max(cur, arr[j])
                j += 1
            if j < n:
                temp = arr[j]
                while j < n and arr[j] < 0:
                    temp = max(temp, arr[j])
                    j += 1
                res += temp + cur
            else:
                res += cur
        elif arr[j]<0:
            temp = arr[j]
            while j < n and arr[j] < 0:
                temp = max(temp, arr[j])
                j += 1
            if j < n:
                cur = arr[j]
                while j < n and arr[j] >0:
                    cur = max(cur, arr[j])
                    j += 1
                res += temp + cur
            else:
                res += temp
    print(res)
    
