class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0] 
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)
        

    def sumRange(self, left: int, right: int) -> int:
        
        leftsum = self.prefix[left]
        rightsum = self.prefix[right + 1]
        return rightsum - leftsum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)