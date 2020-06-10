class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        val = root.val
        return self.DFS(root, val)
        
    """
    A depth-first search on the tree to check each node
    """
    def DFS(self, node, value):
        if node == None:
            return True
        if node.val != value:
            return False
        else:
            left = self.DFS(node.left, value)
            right = self.DFS(node.right, value)
            return left and right
