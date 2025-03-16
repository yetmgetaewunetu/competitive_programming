# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestor(self,root,cur_max,cur_min):
        
        if not root:
            return cur_max - cur_min

        cur_max = max(cur_max,root.val)
        cur_min = min(cur_min,root.val)

        max1 = self.maxAncestor(root.left,cur_max,cur_min)
        max2 =  self.maxAncestor(root.right,cur_max,cur_min)
        
        return max(max1,max2)
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.maxAncestor(root,root.val,root.val)