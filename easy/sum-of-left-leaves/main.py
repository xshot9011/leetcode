# https://leetcode.com/problems/sum-of-left-leaves/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def getSumLeftLeaves(node, isLeave = False):
            if node is None:
                return 0

            if node.left is None and node.right is None and isLeave:
                return node.val
            return getSumLeftLeaves(node.left, True) + getSumLeftLeaves(node.right)

        # Time: O(n)
        # Space: O(1)
        return getSumLeftLeaves(root)
