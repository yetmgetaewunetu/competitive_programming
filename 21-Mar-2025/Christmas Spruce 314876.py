# Problem: Christmas Spruce - https://codeforces.com/contest/913/problem/B

from collections import defaultdict
v = int(input())
arr = [int(input()) for i in range(v-1)]
counter = 2


mydict = defaultdict(list)

for i in range(v-1):
    mydict[arr[i]].append(counter)
    counter += 1
    

arr = list(mydict.keys())
def checker(idx):
    cnt = 0
    if idx >= len(arr):
        return
    for i in mydict[arr[idx]]:
        if i not in mydict:
            cnt += 1
    if cnt < 3:
        return "No"
    return checker(idx + 1)
    
result  = checker(0)

res = result if result else "Yes"
print(res)