# https://leetcode.com/problems/subtree-of-another-tree/
# Comparing Tree has some issue with null 4 - 1 2  and  4 1 null null 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSubNode(node: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            p_queue = []
            q_queue = []
            if node:
                p_queue = [node]
            if subRoot:
                q_queue = [subRoot]
            while len(p_queue) > 0 and len(q_queue) > 0: 
                currentPointer = p_queue.pop(0)
                subRootPointer = q_queue.pop(0)
                if currentPointer.val != subRootPointer.val:
                    return False
                # Cleaning up None issue
                elif currentPointer.left is not None and subRootPointer.left is None:
                    return False
                elif currentPointer.left is None and subRootPointer.left is not None:
                    return False
                elif currentPointer.right is not None and subRootPointer.right is None:
                    return False
                elif currentPointer.right is None and subRootPointer.right is not None:
                    return False
                if currentPointer.left:
                    p_queue.append(currentPointer.left)
                    q_queue.append(subRootPointer.left)
                if currentPointer.right:
                    p_queue.append(currentPointer.right)
                    q_queue.append(subRootPointer.right)
            if len(p_queue) != len(q_queue):
                return False
            return True

        if root is None:
            return False
        
        nodePointers = [root]

        while len(nodePointers):
            currentPointer = nodePointers.pop(0)
            if currentPointer.val == subRoot.val:
                if isSubNode(currentPointer, subRoot):
                    return True
            if currentPointer.left:
                nodePointers.append(currentPointer.left)
            if currentPointer.right:
                nodePointers.append(currentPointer.right)

        return False
