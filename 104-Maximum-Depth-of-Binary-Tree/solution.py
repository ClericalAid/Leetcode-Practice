# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.DFS_depth(root, 0)

    """
    DFS_depth
    A depth-first search which keeps track of the depth of the node
    """
    def DFS_depth(self, node, depth):
        if node == None:
            return depth
        leftDepth = self.DFS_depth(node.left, depth + 1)
        rightDepth = self.DFS_depth(node.right, depth + 1)
        return max(leftDepth, rightDepth)
