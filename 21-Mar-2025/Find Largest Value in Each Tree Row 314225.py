# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def largestInRow(node,depth):
            
            if not node:
                return
            if depth >= len(res):
                res.append(node.val)
            else:
                res[depth] = max(res[depth], node.val)
            
            largestInRow(node.left,depth+1)
            largestInRow(node.right,depth+1)
        largestInRow(root,0)
        return res
            