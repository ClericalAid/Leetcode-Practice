import collections

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = collections.defaultdict(lambda: -1)
        answer = self.recurse(coins, amount, memo)
        if answer == float('inf'):
            return -1
        else:
            return answer

    """
    recurse
    The recursion essentially goes down to 0, and then builds itself back up as the recursion
    goes back up the chain. After reaching 0, anywhere we go from 0 is the minimum amount of coins
    to get to that denomination. It is very difficult to describe

    For each coin denomination
        Subtract that from the amount
        Take our new amount and pass it down the recursion
        
    """
    def recurse(self, coins, amount, memo):
        if memo[amount] != -1:
            return memo[amount]

        if amount < 0:
            return float('inf')
        if amount == 0:
            return 0

        coinAmounts = []
        for coin in coins:
            newAmount = amount - coin
            coinAmounts.append(self.recurse(coins, newAmount, memo))
        memo[amount] = min(coinAmounts) + 1
        return memo[amount]
