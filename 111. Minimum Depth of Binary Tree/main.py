# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def getMinDept(node):
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return 1
            if node.left is None:
                return 1 + getMinDept(node.right)
            if node.right is None:
                return 1 + getMinDept(node.left)
            return 1 + min(getMinDept(node.left), getMinDept(node.right))
        
        return getMinDept(root)
