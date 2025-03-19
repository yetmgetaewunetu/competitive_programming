# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def sumNodes(node,res):
            if not node:
                return []
            fin = []
            res.append(str(node.val))
            if not node.left and not node.right:
                return [int("".join(res))]
            temp= res[:]
            fin.extend(sumNodes(node.left,res))
            fin.extend(sumNodes(node.right,temp))
            return fin
        arr = sumNodes(root,[])
        return sum(arr)