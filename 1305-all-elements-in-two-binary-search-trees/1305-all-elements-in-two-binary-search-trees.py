# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
       
        res =[]
        def inorder(root):
            cur = root
            if root!= None:
                res.append(root.val)
                inorder(root.left)
                inorder(root.right)
        ans1 = inorder(root1)
        ans2 = inorder(root2)
        
        res.sort()
        return res
        