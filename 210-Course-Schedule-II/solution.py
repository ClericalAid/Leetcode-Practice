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

        for cc in prerequisites:
            graph[cc[1]].append(cc[0])

        topArr = []
        visited = collections.defaultdict(lambda: 0)
        node = 0
        while len(topArr) < numCourses:
            loopDet = collections.defaultdict(lambda: 0)
            if visited[node] == 0:
                if self.topSort(graph, topArr, visited, loopDet, node) == False:
                    return []
            node += 1
        topArr.reverse()
        return topArr

    """
    Perform a topological sort on the graph with loop detection

    Before anything happens, we increment the amount of times we have visited this node by 1
    If we have visited this node more than once, we have a loop

    Visit each child that has yet to be visited
    """
    def topSort(self, graph, top, visited, loopDet, node):
        loopDet[node] += 1
        if loopDet[node] > 1:
            return False
        for child in graph[node]:
            if visited[child] == 0:
                if self.topSort(graph, top, visited, loopDet, child) == False:
                    return False
        visited[node] += 1
        top.append(node)

numCourses = 2
prereq = [[1,0], [0,1]]

solver = Solution()
ans = solver.findOrder(numCourses, prereq)
print(ans)

