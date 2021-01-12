import pdb
class Solution:
    def PredictTheWinner(self, nums) -> bool:
        memo = dict()
        return self.recursiveWinFinder(nums, memo, 0, len(nums) - 1, True) >= 0

    """
    Recursive solution. We need to know (when optimally played), which player comes out
    the winner

    Input these variables:
    pointer1, pointer 2
        Designate the new subarray of coins which we are dealing with. If they are equal, there
        is one coin left.
        If pointer1 > pointer2, we have gone through the array. We need to sanitize beforehand?

    player1Turn
        Is true if it's player 1's turn (1 or -1)

    Returns:
        An integer depicting the difference in winnings of player1 - player2. If player 2 wins
        more than player 1, then the returned number is negative

    Base case:
    pointer1 == pointer2
        Return the number they point towards

    player2 wants min
    player1 wants max
    """
    def recursiveWinFinder(self, nums, memo, pointer1, pointer2, player1Turn):
        if (pointer1, pointer2) in memo:
            return memo[(pointer1, pointer2)]

        if pointer1 == pointer2:
            if player1Turn:
                return nums[pointer1]
            else:
                return -1*nums[pointer1]

        if player1Turn:
            leftAnswer = self.recursiveWinFinder(nums, memo, pointer1 + 1, pointer2, False) + nums[pointer1]
            rightAnswer = self.recursiveWinFinder(nums, memo, pointer1, pointer2 - 1, False) + nums[pointer2]
            memo[(pointer1, pointer2)] = max(leftAnswer, rightAnswer)

        else:
            leftAnswer = self.recursiveWinFinder(nums, memo, pointer1 + 1, pointer2, True) - nums[pointer1]
            rightAnswer = self.recursiveWinFinder(nums, memo, pointer1, pointer2 - 1, True) - nums[pointer2]
            memo[(pointer1, pointer2)] = min(leftAnswer, rightAnswer)

        return memo[(pointer1, pointer2)]
