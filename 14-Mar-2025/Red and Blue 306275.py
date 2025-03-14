# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

t = int(input())
for _ in range(t):
    n= int(input())
    arr = list(map(int,input().split()))
    m = int(input())
    arr2 = list(map(int,input().split()))
    cur1 = cur2 = res1 = res2 = 0

    for i in arr:
        cur1 += i
        res1 = max(res1,cur1)
    for i in arr2:
        cur2 += i
        res2 = max(res2,cur2)
    print(res1 + res2)