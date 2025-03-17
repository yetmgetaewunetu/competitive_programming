# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node= TreeNode(val)
        dummy = TreeNode(float('inf'))
        dummy.left = root
        cur = dummy
        while cur:
            if val < cur.val:
                if not cur.left:
                    cur.left = node
                    break
                cur = cur.left
            else:
                if not cur.right:
                    cur.right = node
                    break
                cur = cur.right
        return dummy.left
            