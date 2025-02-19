# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

n,k,q = map(int, input().split())
arr = [0]*(200002)
for i in range(n):
    a,b = map(int,input().split())
    arr[a] += 1
    arr[b+1] -= 1
for i in range(1,len(arr)):
    arr[i] += arr[i-1]
for i in range(len(arr)):
    if arr[i] < k:
        arr[i] = 0
    else:
        arr[i] = 1
for i in range(1,len(arr)):
    arr[i] += arr[i-1]
for j in range(q):
    a,b = map(int,input().split())
    print(arr[b] - arr[a-1])