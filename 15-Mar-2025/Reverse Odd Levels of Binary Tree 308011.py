# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOdd(self,left,right):
        if not left:
            return
        left.val,right.val = right.val, left.val
        if left.left:
            self.reverseOdd(left.left.left,right.right.right)
            self.reverseOdd(left.left.right,right.right.left)
            self.reverseOdd(left.right.left,right.left.right)
            self.reverseOdd(left.right.right,right.left.left)


        

    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.reverseOdd(root.left,root.right)
        return root