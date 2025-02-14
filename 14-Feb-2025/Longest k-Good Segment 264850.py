# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

a,b = map(int,input().split())
arr = list(map(int,input().split()))
window = {}
res = [1,1]
left = 0
for r in range(a):
    window[arr[r]] = window.get(arr[r],0) + 1
    while len(window) > b:
        window[arr[left]] -=1
        if window[arr[left]] == 0:
            del window[arr[left]]
        left += 1
    if res[-1] - res[0] < r-left:
        res = [left+1,r+1]
print(*res)