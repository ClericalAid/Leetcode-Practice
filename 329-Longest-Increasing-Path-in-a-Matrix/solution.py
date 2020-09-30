class Solution:
    """
    I think this is a DP/ recursion problem.

    For each grid in the square:
        Recurse down to its neighbours to which it can travel, and look at those path lengths
        Take the longest one and add 1 to it
        This should recurse all the way down
        This works best if we know where it starts, otherwise we are doing this over every square

    The property of the longest increasing path:
        The ending is a location where the path can no longer continue (if it could continue, then
        that means we are not ending the longest path)
        The beginning is a location where there is no way to get to that square (you can't come in
        from any other direction. Similar theory to above)
        Therefore, if we find all the potential endings i.e. squares which are dead-ends then
        one of those is connected to the longest path

    Double for loop
    Recursion + memo
    Success

    Loop through each square in the grid:
        Look at its neighbours:
            if neighbour > current grid
                We look at max length of this neighbour
            if neighbour <= current grid
                We can't go down this path
        Take the max length found amongst its elligible neighbours and add 1 to it
        Save this answer in a memo
    """
    def longestIncreasingPath(self, matrix) -> int:
        memo = []
        for i in range(len(matrix)):
            memo.append([-1] * len(matrix[0]))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if memo[i][j] == -1:
                    self.recurse(i, j, matrix, memo)
        maxArray = [0]
        for array in memo:
            maxArray.append(max(array))
        return max(maxArray)
    """
    Perform a recursion on elligible neighbours
    Elligible neighbours are within the bounds of the matrix, and contain a number greater than
    the current number
    """
    def recurse(self, i, j, matrix, memo):
        if memo[i][j] != -1:
            return memo[i][j]
        childrenPaths = [0]
        # right
        if (j + 1 < len(matrix[0])):
            if (matrix[i][j + 1] > matrix[i][j]):
                childrenPaths.append(self.recurse(i, j + 1, matrix, memo))
        # left
        if (j - 1 >= 0):
            if (matrix[i][j - 1] > matrix[i][j]):
                childrenPaths.append(self.recurse(i, j - 1, matrix, memo))
        # down
        if (i - 1 >= 0):
            if (matrix[i - 1][j] > matrix[i][j]):
                childrenPaths.append(self.recurse(i - 1, j, matrix, memo))
        # up
        if (i + 1 < len(matrix)):
            if (matrix[i + 1][j] > matrix[i][j]):
                childrenPaths.append(self.recurse(i + 1, j, matrix, memo))
        memo[i][j] = max(childrenPaths) + 1
        return memo[i][j]
