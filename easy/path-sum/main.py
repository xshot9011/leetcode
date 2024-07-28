# https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def hasPathSum(node, cumulative):
            if node is None:
                return False
            cumulative += node.val
            if cumulative == targetSum and node.left is None and node.right is None:
                return True

            return hasPathSum(node.left, cumulative) or hasPathSum(node.right, cumulative)

        if root:
            return hasPathSum(root, 0)
        return False
        