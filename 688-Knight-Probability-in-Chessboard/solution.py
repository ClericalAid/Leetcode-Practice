import collections
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        memo = collections.defaultdict(lambda: -1)
        return self.DFS(N, K, r, c, memo)
        #return memo[(K, r, c)]

    """
    DFS
    Depth-first search with memoization.

    Here are the base cases:
    1)  We have it in our memo
        Return it

    2)  We are out of bounds already
        Return 0 (0% probability, because the knight stops moving after going off the board)

    3)  We are out of moves (K == 0)
        Return 1 (we should be on the board because of the checks in step 2)

    4)  We are not out of bounds
        For every new position which the knight can take
            Recurse/ DFS on said position
            Note: Each new position is a combination of
            +-2, +-1
            +-1, +-2
        Take all the probabilities (8 of them), and average them out, because the knight moves
        in a uniform random manner
    """
    def DFS(self, N, K, r, c, memo):
        # 1)
        if memo[(K, r, c)] != -1:
            return memo[(K, r, c)]

        # 2)
        if r > N - 1 or r < 0:
            return 0
        if c > N - 1 or c < 0:
            return 0

        # 3)
        if K == 0:
            return 1

        # 4)
        probs = []
        probs.append(self.DFS(N, K - 1, r - 2, c - 1, memo))
        probs.append(self.DFS(N, K - 1, r - 2, c + 1, memo))
        probs.append(self.DFS(N, K - 1, r + 2, c - 1, memo))
        probs.append(self.DFS(N, K - 1, r + 2, c + 1, memo))

        probs.append(self.DFS(N, K - 1, r - 1, c - 2, memo))
        probs.append(self.DFS(N, K - 1, r - 1, c + 2, memo))
        probs.append(self.DFS(N, K - 1, r + 1, c - 2, memo))
        probs.append(self.DFS(N, K - 1, r + 1, c + 2, memo))

        memo[(K, r, c)] = sum(probs) / len(probs)
        return memo[(K, r, c)]
