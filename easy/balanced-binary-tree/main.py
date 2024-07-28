# https://leetcode.com/problems/contains-duplicate-ii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getDept(node) -> bool:
            if node is None:
                return 0
            return 1 + max(getDept(node.left), getDept(node.right))

        if root is None:
            return True

        leftDept = getDept(root.left)
        rightDept = getDept(root.right)
        print(f'leftDept: {leftDept}, rightDept: {rightDept}')
        if abs(leftDept - rightDept) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right) # checking subtree
