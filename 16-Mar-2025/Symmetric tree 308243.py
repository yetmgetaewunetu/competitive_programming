# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def symmetric(self,left,right):
        if not left and not right:
            return
        if not (left and right):
            return False

        if left.val != right.val:
            return False
        
        res = self.symmetric(left.left,right.right)

        if res == False:
            return res
        return self.symmetric(left.right,right.left)


    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        res = self.symmetric(root.left,root.right) 
        return True if res == None else False