# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def setInorderPath(node):
            if node is None:
                return
            
            setInorderPath(node.left)
            nodePointers.append(node)
            setInorderPath(node.right)

        def reStructure(left, right) -> TreeNode:
            if left > right:
                return None
            
            mid = (left + right)//2
            nodePointers[mid].left = reStructure(left, mid-1)
            nodePointers[mid].right = reStructure(mid+1, right)
            return nodePointers[mid]

        nodePointers = []
        setInorderPath(root) 
        reStructure(0, len(nodePointers)-1)
        root = nodePointers[(0 + len(nodePointers)-1)//2]
        # Time: O(n) + O(n) = O(n)
        # Space: O(n)
        return root
