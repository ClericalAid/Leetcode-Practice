class Solution:
    """
    Brute force approach:

    For each cell, we:
        Take the max in its row
        Take the max in its col
        Take the minimum of those two values
        That is its new value

    Take the max of every row and col
    Each cell then takes the minumum of the maximum between its row and col
    """
    def maxIncreaseKeepingSkyline(self, grid) -> int:
        rowMax = []
        colMax = []
        colCount = len(grid[0])
        for row in grid:
            rowMax.append(max(row))

        for j in range(colCount):
            col = []
            for row in grid:
                col.append(row[j])
            colMax.append(max(col))

        increase = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                increase += min(rowMax[i], colMax[j]) - grid[i][j]

        return increase
solver = Solution()
inputGrid = [ [3, 0, 8, 4], 
              [2, 4, 5, 7],
              [9, 2, 6, 3],
              [0, 3, 1, 0] ]
print(solver.maxIncreaseKeepingSkyline(inputGrid))

