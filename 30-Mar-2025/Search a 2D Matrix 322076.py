# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low,high = 0,len(matrix) -1
        col = len(matrix[0])

        while low <= high:
            mid = (low + high)//2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                low,high = 0,col-1
               
                while low <= high:
                    middle = (low + high)//2

                    if matrix[mid][middle] == target:
                        return True
                    elif matrix[mid][middle] < target:
                        low = middle +1
                    else:
                        high = middle - 1
                return False
            elif matrix[mid][0] > target:
                high = mid -1
            else:
                low = mid +1
        return False