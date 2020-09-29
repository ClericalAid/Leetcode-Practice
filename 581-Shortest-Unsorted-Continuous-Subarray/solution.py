class Solution:
    """
    The following pattern holds true for an unsorted subarray embedded into a larger array such
    that the subarray being sorted would cause the whole array to be sorted
    [..., i, SUBARRAY, j, ...]
    min(SUBARRAY) >= i
    max(SUBARRAY) <= j

    Find the first case where the number sorting breaks gonig from the beginning
        We look for the first case/ index where the following occurs:
        array[i] > array[i+1]
    Find the first instance of the mirrored case from above, but starting from the end:
        array[j-1] > array[j]
    These two indices designate a subarray where the array is definitely unsorted. After
    finding these two indices we:
    1)  Find the largest number in this subarray
    2)  Find the smallest number in this subarray
    3)  Proceed to the right and begin expanding the subarray by comparing the max of the
        subarray, to the numbers to the right
    4)  Repeat step 3 but for the left

    In summary:
    1)  Find the first instance where the sorted array "breaks" starting from beginning
    2)  Find the first instance where the sorted array "breaks" starting from the end
    3)  Find the max of this subarray between pointer1 and pointer2
    4)  Find the min of this subarray between pointer1 and pointer2
    5)  Grow the subarray to the left
    6)  Grow the subarray to the rightt
    """
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        if self.array_sorted(nums):
            return 0
        # 1)
        begPointer = self.find_beginning(nums)

        # 2)
        endPointer = self.find_ending(nums)

        # 3)
        if begPointer > endPointer:
            minNum = nums[begPointer]
        else:
            minNum = min(nums[begPointer:endPointer + 1])

        # 4)
        if begPointer > endPointer:
            maxNum = nums[endPointer]
        else:
            maxNum = max(nums[begPointer:endPointer + 1])

        # 5)
        beginningUnsorted = self.grow_left(nums, begPointer, minNum)

        # 6)
        endUnsorted = self.grow_right(nums, endPointer, maxNum)

        print(beginningUnsorted)
        print(endUnsorted)
        return endUnsorted - beginningUnsorted - 1

    
    def array_sorted(self, nums):
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return False
        return True

    def find_beginning(self, nums):
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                break
        return i

    def find_ending(self, nums):
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] < nums[i - 1]:
                break
        return i

    def grow_left(self, nums, startPointer, minNum):
        iterPointer = startPointer - 1
        while iterPointer >= 0 and nums[iterPointer] > minNum:
            iterPointer -= 1
        return iterPointer

    def grow_right(self, nums, startPointer, maxNum):
        iterPointer = startPointer + 1
        while iterPointer < len(nums) and nums[iterPointer] < maxNum:
            iterPointer +=1
        return iterPointer

inp1 = [1, 3, 5, 4, 2]
solver = Solution()
solver.findUnsortedSubarray(inp1)
