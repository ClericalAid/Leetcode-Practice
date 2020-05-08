# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    Breadth-first search approach. But when we find an even number, we will
    get the sum of its grandchildren.

    The breadth-first search is performed as follows:

    1)
    Push the given node into a queue

    2)
    Perform loop until the queue is empty:
        Pop the first node from the queue
        If the node is legitimate:
            Add its children to the end of the queue
            Check if it is even, and if it is, then we take the sum of its
            grandchildren and add it to our running total
        Otherwise:
            Continue the loop
    """
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        queue = []
        queue.append(root)
        totalSum = 0
        while len(queue) != 0:
            currNode = queue.pop(0)
            if currNode != None:
                queue.append(currNode.left)
                queue.append(currNode.right)
                if currNode.val % 2 == 0:
                    totalSum += self.get_grandchildren(currNode)
            else:
                pass
        return totalSum
    
    """
    Returns the sum of the grand children of the given node
    Brute force check if the grandchildren exist, and if it does, we add it to
    a running total which we keep track of
    """
    def get_grandchildren(self, node):
        retSum = 0
        if node.left != None:
            if node.left.left != None:
                retSum += node.left.left.val
            if node.left.right != None:
                retSum += node.left.right.val
        if node.right != None:
            if node.right.left != None:
                retSum += node.right.left.val
            if node.right.right != None:
                retSum += node.right.right.val
        return retSum
