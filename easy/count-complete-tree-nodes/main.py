# https://leetcode.com/problems/count-complete-tree-nodes/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def countNode(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            countNode(node.left)
            nonlocal counter
            counter += 1
            countNode(node.right)
        
        counter = 0
        countNode(root)
        return counter
