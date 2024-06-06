# https://leetcode.com/problems/diameter-of-binary-tree/
# TBH, I hate this one hahahahahah, take too much time


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0
        def setMaxDiameter(node: Optional[TreeNode]) -> int:
            nonlocal maxDiameter
            if node is None:
                return -1
            rightHeight = 1 + setMaxDiameter(node.right)
            leftHeight = 1 + setMaxDiameter(node.left)
            print(f'rightHeight: {rightHeight}, leftHeight: {leftHeight}, maxDiameter: {maxDiameter}')
            maxDiameter = max(maxDiameter, rightHeight+leftHeight)
            return max(rightHeight, leftHeight) # return max path A that can go
        
        setMaxDiameter(root)
        return maxDiameter
