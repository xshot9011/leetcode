# https://leetcode.com/problems/binary-tree-paths/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def levelOrderSearch(node, path=None) -> None:
            if node is None:
                return

            if path is None:
                path = str(node.val)
            else:
                path += "->" + str(node.val)
            
            if node.left is None and node.right is None: # leaf
                ans.append(path)
            else:
                levelOrderSearch(node.left, path)
                levelOrderSearch(node.right, path)
            
        ans = []
        levelOrderSearch(root)
        return ans
