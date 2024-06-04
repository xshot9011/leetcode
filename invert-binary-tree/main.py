# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        treeQueue = [root]
        ansTree = TreeNode()
        ansQueue = [ansTree]
        while len(treeQueue) >= 1:
            currentPointer = treeQueue.pop(0)
            ansPointer = ansQueue.pop(0)
            ansPointer.val = currentPointer.val

            if currentPointer.right:
                treeQueue.append(currentPointer.right)
                ansPointer.left = TreeNode()
                ansQueue.append(ansPointer.left)
            if currentPointer.left:
                treeQueue.append(currentPointer.left)
                ansPointer.right = TreeNode()
                ansQueue.append(ansPointer.right)
        
        return ansTree

"""
# AHHHHHH
parent -> left, right
childLeft = parent.left
parent.left = self.x(parent.right)
parent.right = self.x(childLeft)
"""
