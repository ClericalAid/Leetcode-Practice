import collections

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = collections.defaultdict(lambda: 0)
        return self.recurse(n, memo)
    
    def recurse(self, n, memo):
        if memo[n] != 0:
            return memo[n]

        if n < 0:
            return 0

        elif n == 0:
            return 1

        else:
            memo[n] += self.recurse(n - 1, memo)
            memo[n] += self.recurse(n - 2, memo)

        return memo[n]


solver = Solution()
print(solver.climbStairs(4))
