# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        inorder(root)
        root = TreeNode(arr[len(arr)//2])
        def constructBST(cur,l,r):
            if l > r:
                return
            mid = (l + r)//2
            node = TreeNode(arr[mid])
            node.left = constructBST(node,l,mid-1)
            node.right = constructBST(node,mid+1,r)

            return node
        
        return constructBST(root,0,len(arr)-1)
        
