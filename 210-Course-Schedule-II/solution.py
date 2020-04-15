import collections
import pdb
class Solution:
    """
    Place courses into a directed graph
    Each node has an array of neighbour, and points at courses that it leads up to
    If course 2 requires both course 1 and 0, then the graph would look like:
        [[2], [2], []]

    We then perform a topological sort on our graph, and also include a loop detector.
    We cycle through each node and call a topological sort on it, if it has yet to be visited
    """
    def findOrder(self, numCourses, prerequisites):
        graph = []
        for i in range(numCourses):
            graph.append([])

        for coursePair in prerequisites:
            graph[coursePair[1]].append(coursePair[0])

        topologicalArr = []
        visited = collections.defaultdict(lambda: 0)
        currNode = 0
        while len(topologicalArr) < numCourses:
            loopDet = collections.defaultdict(lambda: 0)
            if visited[currNode] == 0:
                if self.topSort(graph, topologicalArr, visited, loopDet, currNode) == False:
                    return []
            currNode += 1
        topologicalArr.reverse()
        return topologicalArr

    """
    Perform a topological sort on the graph with loop detection

    Before anything happens, we increment the amount of times we have visited this node
    by 1. If we have visited this node more than once, we have a loop, and we need to exit
    accordingly.

    Visit each child that has yet to be visited
    """
    def topSort(self, graph, topologicalArr, visited, loopDet, node):
        loopDet[node] += 1
        if loopDet[node] > 1:
            return False
        for child in graph[node]:
            if visited[child] == 0:
                if self.topSort(graph, topologicalArr, visited, loopDet, child) == False:
                    return False
        visited[node] += 1
        topologicalArr.append(node)

numCourses = 4
prereq = [[1,0], [2,0], [3,1]]

solver = Solution()
ans = solver.findOrder(numCourses, prereq)
print(ans)

