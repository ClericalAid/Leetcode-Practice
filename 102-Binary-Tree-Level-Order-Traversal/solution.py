# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levelArrays = []

        #self.DFS_level(root, 0, levelArrays)
        self.BFS_level(root, levelArrays)
        return levelArrays

    """
    BFS_level
    A breadth-first search which records the levels of the nodes. It does this by pushing a 'None'
    object into the queue to separate the levels. When we encounter a 'None' object, we push
    another one onto the queue. For a basic, full binary tree of 1, 2, 3, 4, 5, 6, 7
             1
           /   \
          2     3
         / \   /  \
        4  5   6  7 
    We should see at the beginning:
    [1, None]
     ^
     pointer

    Then after the first iteration of the loop, we should now have:
    [1, None, 2, 3, None]
        ^
        pointer

    We end when we have more than one 'None' in a row
    """
    def BFS_level(self, root, levelArrays):
        queue = []
        queuePointer = 0
        depth = 0
        if root == None:
            return

        queue.append(root)
        queue.append(None)
        while queuePointer < len(queue):
            currNode = queue[queuePointer]
            queuePointer += 1
            if currNode == None:
                depth += 1
                if queue[queuePointer - 2] == None:
                    return
                queue.append(None)
            else:
                if len(levelArrays) <= depth:
                    levelArrays.append([])

                if currNode.left != None:
                    queue.append(currNode.left)
                if currNode.right != None:
                    queue.append(currNode.right)
                levelArrays[depth].append(currNode.val)
            

    """
    DFS_level
    A depth-first search where we keep track of the level
    """
    def DFS_level(self, node, depth, levelArrays):
        if node == None:
            return
        if len(levelArrays) <= depth:
            levelArrays.append([])
        levelArrays[depth].append(node.val)
        self.DFS_level(node.left, depth + 1, levelArrays)
        self.DFS_level(node.right, depth + 1, levelArrays)
