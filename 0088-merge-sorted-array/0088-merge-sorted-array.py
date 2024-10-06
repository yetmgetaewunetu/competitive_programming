class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = j = k = 0
        while i < m and j < n:
            if nums1[i] > nums2[j]:
                nums1.insert(k, nums2[j])
                i += 1
                j += 1
                m += 1
                nums1.pop()
            else:
                
                i += 1

            k += 1
        while i < m:
            nums1[k] = nums1[i]
            i += 1
            k += 1
        while j < n:
            nums1[k] = nums2[j]
            j += 1
            k += 1