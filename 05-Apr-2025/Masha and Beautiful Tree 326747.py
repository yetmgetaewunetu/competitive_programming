# Problem: Masha and Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

class Solution:

        def __init__(self, arr):
              self.res = -1
              self.arr = arr

        def merge(self,l,r,mid):

            
            if self.arr[l] > self.arr[mid]:
                self.res += 1

                j = mid

                while l < mid and j <= r:
                    self.arr[l], self.arr[j] = self.arr[j], self.arr[l]
                    l += 1
                    j += 1

            return 

        def mergeSort(self,l,r):
            if r - l < 1:
                return self.res

            mid = l + (r - l) //2
            # print(l,r,mid)
            self.mergeSort(l, mid)
            self.mergeSort(mid + 1, r)

            self.merge(l,r,mid + 1)

            return self.res
        
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    
    solution =  Solution(arr)
    ans = solution.mergeSort(0,n - 1)

    # print(ans,arr)
    
    if arr == sorted(arr):
        print(ans + 1)
    else:
        print(-1)