# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

t =int(input())
arr = list(map(int,input().split()))
arr.sort()
if not t%2:
    print(arr[t//2 - 1])
else:
    print(arr[t//2])
