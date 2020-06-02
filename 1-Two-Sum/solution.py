import collections

class Solution:
    """
    parameters:
    nums - list of integers
    target - the number which we wish to sum to

    Store all of the values of the list into a dictionary
    Iterate through the list again keeping track of our location with the variable 'i'
    For each number in the list, we check if the complementary number exists. That is, we check
    the dictionary for the key:
        target - nums[i]
    If this key exists, then that means that there are 2 numbers in the list which add up to the
    target number

    Special case:
    We are not allowed to reuse indices, so if we have the same index, we do not return it
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookUp = collections.defaultdict(lambda: -1)
        for i in range(len(nums)):
            lookUp[nums[i]] = i
        for i in range(len(nums)):
            newTarget = target - nums[i]
            if newTarget in lookUp:
                if lookUp[newTarget] != i:
                    return [i, lookUp[newTarget]]
