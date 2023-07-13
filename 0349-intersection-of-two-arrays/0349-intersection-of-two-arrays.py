class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        List = []
        var = nums2
        var1 = nums1
       
        if len(nums1) < len(nums2):
            var= nums1
            var1 = nums2
        for i in range(len(var)):
            if var[i] in var1 and var[i] not in List:
                List.append(var[i])
        return List