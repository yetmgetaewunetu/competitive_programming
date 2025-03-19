# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if max(p.val,q.val) < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif min(p.val,q.val) > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root





        # res = root
        # def lowestCommon(node,res):
        #     if max(p.val,q.val) < node.val:
        #         res = lowestCommon(node.left,res)
        #     elif min(p.val,q.val) > node.val:
        #         res = lowestCommon(node.right,res)
        #     else:
        #         return node
        #     return res

        # return lowestCommon(root,res)
        