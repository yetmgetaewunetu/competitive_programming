class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1)%2 == 0:
            x = int(len(nums1)/2)
            return (nums1[x]+nums1[x-1])/2
        elif len(nums1) % 2 ==1:
            y = int((len(nums1)-1)/2)
            return nums1[y]