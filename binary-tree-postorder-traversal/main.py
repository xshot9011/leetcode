# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorder(node: Optional[TreeNode], nodeList: List[int]) -> List[int]:
            if node is None:
                return
            postorder(node.left, nodeList)
            postorder(node.right, nodeList)
            nodeList.append(node.val)
        
        nodeList = []
        postorder(root, nodeList)
        return nodeList
