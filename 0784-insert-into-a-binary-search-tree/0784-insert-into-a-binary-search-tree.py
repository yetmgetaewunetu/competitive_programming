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
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = node
                    return dummy.left
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = node
                    return dummy.left
        return dummy.left
            