class Solution:
    def solveNQueens(self, n: int):
        queenLocations = []
        solutions = []
        self.DFS(n, queenLocations, solutions, 0)
        return solutions

    """
    DFS
    The layout of queens is like a tree
    For each queen we add, there is another layer to the tree

    Base case:
    We have filled the board, return the solution

    Otherwise:
    1)  Loop through the column and try to add a queen
        2)  Check it's validity, with respect to other queens (save a list of queen locations?)
            Return if the queen is not valid
            a)  Check row against the other queen
            b)  Check diagonals
        3)  If valid, we go down the chain by trying to place a queen at the next column
    """
    def DFS(self, n, queenLocations, solutions, column):
        if column >= n:
            listAnswer = []
            stringAnswer = []
            for i in range(n):
                listAnswer.append(["."]*n)
            for queen in queenLocations:
                listAnswer[queen[0]][queen[1]] = "Q"
            for subList in listAnswer:
                stringAnswer.append("".join(subList))
            solutions.append(stringAnswer)
            return

        # 1)
        for i in range(n):
            invalidQueen = False
            row = i
            # 2)
            for queen in queenLocations:
                # a)
                if queen[1] == row:
                    invalidQueen = True
                # b)
                elif abs(queen[0] - column) == abs(queen[1] - row):
                    invalidQueen = True
            # 3)
            if invalidQueen == False:
                queenLocations.append([column, row])
                self.DFS(n, queenLocations, solutions, column + 1)
                queenLocations.pop()
        pass
