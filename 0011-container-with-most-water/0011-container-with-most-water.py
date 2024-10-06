class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right = 0, len(height) -1 
        maximum = 0
        while left < right:
            temp = min(height[left],height[right]) * (right - left)
            maximum = max(maximum, temp)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maximum
