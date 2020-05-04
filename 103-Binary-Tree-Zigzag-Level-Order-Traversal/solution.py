class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Print a tree in zig zag pattern, level by level. This means that every other layer
    of the tree is read backwards. For example, given the following tree:
        3
       / \
      9  20
        /  \
       15   7

    The zigzag level order traversal would be:
    [3]
    [20, 9]
    [15, 7]

    We use breadth-first search, but also include a marker which we push into the
    queue, to allow us to keep track of the different levels. The marker we will use
    is Python's None object. We place the None object after the root node. Then,
    whenever we encounter a None object, we push a None object to the end of the
    queue. Therefore, these None objects will work as a flag to separate the different
    levels

    The breadth first search while loop will be as follows:
        Pop the next node from the queue

        Case 1) The node is "None":
            If this is a second "None" in a row 
                Break the loop, we have reached the end of the tree
            We know that we have reached the end of the current level
            Print out our nodes backwards or forwards depending on the level
            Put a None object at the end of the queue to mark the end of the next level
            Take note of the fact that we have found a None object
            
        Case 2) The node is real:
            Place its children at the end of the queue
            Take this node and put it into a temp array of all nodes at this level
    """
    def zigzagLevelOrder(self, root: TreeNode):
        queue = []
        zigzag = []
        levelArray = []
        queue.append(root)
        queue.append(None)

        finishedExploring = False
        forwards = True
        noneCounter = 0
        while finishedExploring == False:
            curr = queue.pop(0)

            # Case 1)
            if curr == None:
                noneCounter += 1
                if forwards == False:
                    levelArray.reverse()
                if len(levelArray) > 0:
                    zigzag.append(levelArray.copy())
                levelArray.clear()
                queue.append(None)
                if noneCounter == 2:
                    finishedExploring = True
                
                if forwards == False:
                    forwards = True
                else:
                    forwards = False

            # Case 2)
            else:
                noneCounter = 0
                levelArray.append(curr.val)
                if curr.left != None:
                    queue.append(curr.left)
                if curr.right != None:
                    queue.append(curr.right)

        return zigzag

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solver = Solution()
ans = solver.zigzagLevelOrder(root)
print(ans)
