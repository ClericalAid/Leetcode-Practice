class Solution:
    """
    Problems:
    Changing array[i + 1] to array[i] isn't always the solution, because sometimes we need to change
    array[i] to array[i + 1]. For example:
    4, 2, 3

    Counting the amount of "fails" doesn't work either, because we need to see the magnitude
    of the breaking point. For example, the following sequence only has one point of failure -
    going from 5 to 1. However, every number after 1 fails as well, causing the whole sequence to
    fail.
    4, 5, 1, 2, 3

    Brute force solution:
    Go through the array, and count the discepancies. 
    
    Case 1)
    If it is greater than 2, then false.

    Case 2)
    If there is only 1 discrepancy, we need to test if said discrepancy is fixable in one step.
        Fix the discrepancy in 2 ways and and then test them.
        1)
        Set array[i + 1] = array[i]

        2)
        Set array[i] = array[i + 1]
        
        Then retest both new arrays (or at least test the 4 values from i - 1 to i + 2). We do
        not need to retest the whole array.

    Possible Improvements:
        Instead of using memory and restesting the arrays, we can take this one step further. 

        Since we would normally transform the value at index 'i' into the value at index 
        'i + 1' or vice-versa, before testing the arrays again - we can instead test those values
        directly to the array without changing them.

        if array[i] > array[i + 1]
            1)
            Make sure array[i + 1] >= array[i - 1]
                This test covers the case where we turn array[i] into array[i + 1]
            2)
            Make sure array[i + 2] >= array[i]
                This test covers the case where we turn array[i + 1] into array[i]

        Here's an example to help us out:
        4, 5, 1, 2
        
        In 1) we set array[i + 1] to array[i]
        In 2) we set array[i] to array[i + 1]
        1) 
        4, 5, 5, 2

        2)
        4, 1, 1, 2
     """
    def checkPossibility(self, nums) -> bool:
        problemCounter = 0
        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i]:
                problemCounter += 1
                if i == 0:
                    continue
                elif i + 2 == len(nums):
                    continue
                else:
                    if nums[i + 1] >= nums[i - 1]:
                        nums[i] = nums[i + 1]
                    elif nums[i + 2] >= nums[i]:
                        nums[i + 1] = nums[i]
                    else:
                        problemCounter += 1
                pass
        if problemCounter > 1:
            return False
        return True

inputArray = [-1, 4, 2, 3]
solver = Solution()
print(solver.checkPossibility(inputArray))
