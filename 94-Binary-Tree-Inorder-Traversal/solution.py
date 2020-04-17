class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    Inorder traversal is:
    1) Left child (recursive call)
    2) This node
    3) Right child (recursive call)
    
    This sorts the tree by constantly returning the "left most" node at each step
    """
    def inorderTraversal(self, root):
        nodeList = []
        self.inorderRecurse(nodeList, root)
        return nodeList
    
    def inorderRecurse(self, nodeList, node):
        if node == None:
            return
        # 1)
        self.inorderRecurse(nodeList, node.left)

        # 2)
        nodeList.append(node.val)

        # 3)
        self.inorderRecurse(nodeList, node.right)

