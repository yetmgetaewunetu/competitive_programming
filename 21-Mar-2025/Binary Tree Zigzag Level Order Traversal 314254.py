# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        flag = True
        res = []
        def traverser(node,depth):
            if not node:
                return 
            if depth >= len(res):
                res.append([node.val])
            else:
                res[depth].append(node.val)
            
            traverser(node.left,depth+1)
            traverser(node.right,depth+1)
        traverser(root,0)
        for i in range(1,len(res),2):
            res[i].reverse()
        return res