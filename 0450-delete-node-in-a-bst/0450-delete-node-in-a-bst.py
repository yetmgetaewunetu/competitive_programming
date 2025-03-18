# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def getSuccessor(node):
            if node.left:
                node = getSuccessor(node.left)
            return node

        if not root:
            return root
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)
        elif root.val > key:
            root.left = self.deleteNode(root.left,key)
        else:
            if not (root.left or root.right):
                return None
            elif root.left and not root.right:
                return root.left
            elif root.right and not root.left:
                return root.right
            else:
                temp = getSuccessor(root.right)
                root.val = temp.val
                temp.val = key
                root.right = self.deleteNode(root.right,key)
                

        return root
        

        

            