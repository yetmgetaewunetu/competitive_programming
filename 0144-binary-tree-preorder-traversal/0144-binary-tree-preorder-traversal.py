# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        arr = [root.val]
        arr.extend(self.preorderTraversal(root.left))
        arr.extend(self.preorderTraversal(root.right))
        return arr