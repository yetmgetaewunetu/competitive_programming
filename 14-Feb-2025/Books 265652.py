# Problem: Books - https://codeforces.com/contest/279/problem/B

a,b = map(int,input().split())
arr = list(map(int,input().split()))
window = l = res = 0
for r in range(a):
    window += arr[r]
    while window > b:
        window -= arr[l]
        l += 1
    res = max(r-l+1, res)
print(res)