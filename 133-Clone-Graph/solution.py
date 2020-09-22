import collections

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return

        visitedNodes = collections.defaultdict(lambda: 0)
        return self.DFS_clone(node, visitedNodes)

    """
    DFS to clone the graph
    If the node exists, we return the node
    If not, we create the node then return it?
    If we do this, we have to go through every connection

    If the amount of connections is n, we are order n
    """
    def DFS_clone(self, node, visited):
        if visited[node.val] != 0:
            return visited[node.val]
        clonedNode = Node(node.val)
        visited[node.val] = clonedNode
        for neighbour in node.neighbors:
            clonedNode.neighbors.append(self.DFS_clone(neighbour, visited))

        return visited[node.val]
            
