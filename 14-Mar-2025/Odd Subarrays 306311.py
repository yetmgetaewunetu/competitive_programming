# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    res  = 0
    cur_max = 0
    for i in arr:
        if cur_max > i:
            res +=1
            cur_max = 0
        else:
            cur_max = i
    print(res)
        