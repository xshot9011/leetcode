# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(node: Optional[TreeNode], nodeList: List[int]) -> List[int]:
            if node is None:
                return
            nodeList.append(node.val)
            preorder(node.left, nodeList)
            preorder(node.right, nodeList)
        
        nodeList = []
        preorder(root, nodeList)
        return nodeList
