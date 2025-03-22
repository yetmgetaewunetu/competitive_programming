# Problem: Convert Sorted Array to Binary Search Tree - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = TreeNode(nums[len(nums)//2])
        def helper(cur,l,r):
            if l > r:
                return
            mid = (l+r)//2
            node = TreeNode(nums[mid])
            node.left = helper(node,l,mid-1)
            node.right = helper(node,mid+1,r)
            return node
        
        return helper(root,0,len(nums)-1)