# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val)
            return root
        if val < root.val:
            if root.left:
                self.insertIntoBST(root.left,val)
            else:
                root.left = TreeNode(val)
        else:
            if root.right:
                self.insertIntoBST(root.right,val)
            else:
                root.right = TreeNode(val)
        return root
        
        # if val < root.val:
        #     root.left = self.insertIntoBST(root.left,val)
        # else:
        #     root.right = self.insertIntoBST(root.right,val)
        
        # return root

        
        
        
        
        # node= TreeNode(val)
        # dummy = TreeNode(float('inf'))
        # dummy.left = root
        # cur = dummy
        # while cur:
        #     if val < cur.val:
        #         if not cur.left:
        #             cur.left = node
        #             break
        #         cur = cur.left
        #     else:
        #         if not cur.right:
        #             cur.right = node
        #             break
        #         cur = cur.right
        # return dummy.left
            