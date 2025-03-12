# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def pascals(self,arr,rowIndex):
        if rowIndex == 0:
            return arr
            
        newArr = [1]*(len(arr)+1)
        for i in range(1,len(arr)):
            if i-1>=0:
                newArr[i] = arr[i-1] + arr[i]
        return self.pascals(newArr,rowIndex-1)

    def getRow(self, rowIndex: int) -> List[int]:
        return self.pascals([1],rowIndex)