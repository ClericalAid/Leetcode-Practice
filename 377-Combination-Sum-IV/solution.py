import collections
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = collections.defaultdict(lambda: -1)
        return self.recurse(nums, target, memo)

    """
    recurse
    Recursive approach where we build up the combinations from 0, upwards

    Base case:
    If we have reached 0, then that means we are at step 1

    For each available number in the list, we subtract said number from our current number
    1)  The result is less than 0
        We move along, nothing to do
    2)  The number is greater than equal to 0
        We can continue down that path, and consider that number as part of the sum
    """
    def recurse(self, nums, currNumber, memo):
        if memo[currNumber] != -1:
            return memo[currNumber]

        if currNumber == 0:
            return 1

        combos = 0
        for number in nums:
            nextNum = currNumber - number
            if nextNum >= 0:
                combos += self.recurse(nums, nextNum, memo)

        memo[currNumber] = combos
        return memo[currNumber]
