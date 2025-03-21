# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res = 0
        cnt = defaultdict(int)
        def average(node):

            nonlocal res,average
            if not node:
                return [0,0]
            
            [left_sum,number_of_node_left] = average(node.left) 
            [right_sum,number_of_node_right] = average(node.right)

            summ = left_sum + right_sum + node.val
            nodes = number_of_node_left + number_of_node_right + 1
            average_val = summ// nodes

            cnt[node.val] += 1
            if average_val == node.val:
                res += 1

            # print(node.val, res,cnt,average_val,summ,nodes)

            return  [summ,nodes]
        average(root)
        return res