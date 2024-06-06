# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Level Order Search
        """
        p_queue = []
        q_queue = []
        if p:
            p_queue = [p]
        if q:
            q_queue = [q]
        while len(p_queue) > 0 and len(q_queue) > 0:
            p_cursor = p_queue.pop(0)
            q_cursor = q_queue.pop(0)
            if p_cursor.val != q_cursor.val:
                return False
            elif p_cursor.left is not None and q_cursor.left is None:
                return False
            elif p_cursor.left is None and q_cursor.left is not None:
                return False
            elif p_cursor.right is not None and q_cursor.right is None:
                return False
            elif p_cursor.right is None and q_cursor.right is not None:
                return False
            if p_cursor.left:
                p_queue.append(p_cursor.left)
                q_queue.append(q_cursor.left)
            if p_cursor.right:
                p_queue.append(p_cursor.right)
                q_queue.append(q_cursor.right)

        if len(p_queue) != len(q_queue):
            return False
        return True
