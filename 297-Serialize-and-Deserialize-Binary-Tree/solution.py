# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """
        Encodes a tree to a single string, using BFS
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return []

        queue = []
        serializedTree = []
        queue.append(root)

        while len(queue) > 0:
            currNode = queue.pop(0)
            if currNode != None:
                serializedTree.append(currNode.val)
                queue.append(currNode.left)
                queue.append(currNode.right)
            else:
                serializedTree.append(None)
                pass
        return serializedTree

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        
        Uses breadth-first search in order to keep track of which node to visit as well as fill out
        the tree

        The main loop works similar to a breadth-first search:
        1)  Pop out the node from the queue
        2)  Create its children from the value in the data array for both the left and right
            side
            
            SPECIAL CASES:
            a) The value was "None"
            It means that this node doesn't have that corresponding child, so we do not
            create a node

            b) The value was not "None"
            We create the node
            We append the node to the queue because we will have to fill out its children in order
        

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None

        queue = []
        rootNode = TreeNode(data.pop(0))
        queue.append(rootNode)
        while len(queue) > 0:
            # 1)
            currNode = queue.pop(0)

            # left
            leftValue = data.pop(0)
            # 2a)
            if leftValue == None:
                currNode.left = None

            # 2b)
            else:
                currNode.left = TreeNode(leftValue)
                queue.append(currNode.left)

            # right
            rightValue = data.pop(0)
            if rightValue == None:
                currNode.right = None
            else:
                currNode.right = TreeNode(rightValue)
                queue.append(currNode.right)
        return rootNode



tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.right.left = TreeNode(4)
tree.right.right = TreeNode(5)

solver = Codec()
serialized = solver.serialize(tree)
deserialized = solver.deserialize(serialized)
deserialized = solver.deserialize([])

"""
print(deserialized.val)
print(deserialized.left.val)
print(deserialized.right.val)
print(deserialized.left.left)
print(deserialized.left.right)
print(deserialized.right.left.val)
print(deserialized.right.right.val)
"""
