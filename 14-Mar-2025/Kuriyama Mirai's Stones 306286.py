# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

n = int(input())
arr = list(map(int,input().split()))
arr2 = arr[:]
arr2.sort()
prefix1 = [0]
prefix2 = [0]
for i in arr:
    prefix1.append(prefix1[-1] + i)
for i in arr2:
    prefix2.append(prefix2[-1] + i)

m = int(input())
for i in range(m):
    c,l,r = map(int,input().split())
    if c == 1:
        print(prefix1[r] - prefix1[l-1])
    else:
        print(prefix2[r] - prefix2[l-1])