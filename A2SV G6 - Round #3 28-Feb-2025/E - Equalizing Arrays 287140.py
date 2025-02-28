# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

n = int(input())
arr = list(map(int,input().split()))
m = int(input())
arr2 = list(map(int,input().split()))

if sum(arr) != sum(arr2):
    print(-1)
    exit()



l1 = l2  = 0
res = 0
win1 = 0
win2 = 0
while l1 < n :
    win1 += arr[l1]
    win2 += arr2[l2]
    l1 += 1
    l2 += 1
    while win1 != win2:
        if win1 < win2:
            win1 += arr[l1]
            l1 += 1
        elif win2 < win1:
            win2 += arr2[l2]
            l2 += 1
    res += 1        
print(res)