# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cur_total = 0
        def makeGreater(node):
            nonlocal cur_total
            if not node:
                return 
            
            # print(node.val,cur_total)
            makeGreater(node.right)
            node.val += cur_total
            cur_total = node.val
            makeGreater(node.left)


        makeGreater(root)
        return root
