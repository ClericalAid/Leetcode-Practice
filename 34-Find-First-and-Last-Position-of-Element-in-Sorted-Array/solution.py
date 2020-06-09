class Solution:
    """
    searchRange
    parameters:
        nums
            The array of numbers
        target
            The target number for which we are searching

    We binary search the first and last digit
    """
    def searchRange(self, nums, target):
        if len(nums) == 0:
            return [-1, -1]
        firstIndex = self.binarySearch(nums, target, first = True)
        lastIndex = self.binarySearch(nums, target, first = False)
        return [firstIndex, lastIndex]

    """
    To binary search the first index, we do the following:
        Binary search and find our number
        Case 1:
            The number we are looking at is less than our number
            We binary search up
        Case 2:
            The number we are looking at is more than our number
            We bianry search down
        Case 3:
            The number we are looking at is our number
            We check the number that comes before it (current index minus 1)
            a)  The number at index - 1 is still the target number
                Binary search down
            b)  The number at index - 1 is not our number
                We found the first index
            c)  We are at index 0 and thus there is no index - 1
                We found the first index, and need to return that
                This gets covered in case 4
        Case 4: (EDGE CASES BABY)
            We reach the last search (left = right)
            If this number is our number, return it, if not we dip
    Binary searching for the last index follows a similar approach but the opposite
    """
    def binarySearch(self, nums, target, first = True):
        left = 0
        right = len(nums) - 1

        numFound = False
        while numFound == False:
            mid = (right + left) // 2
            # Case 4
            if left == right:
                if nums[left] == target:
                    return left
                else:
                    return -1
            # Case 1
            if nums[mid] < target:
                left = mid + 1

            # Case 2
            elif nums[mid] > target:
                right = mid

            # Case 3
            elif nums[mid] == target:
                if first == True:
                    # Case 3a)
                    if nums[mid - 1] == target:
                        right = mid

                    # Case 3b)
                    else:
                        numFound = True
                else:
                    # Case 3a) For the last index
                    if nums[mid + 1] == target:
                        left = mid + 1

                    # Case 3b) For the last index
                    else:
                        numFound = True
        return mid

nums = [5,7,7,8,8,10]
target = 8
solver = Solution()
print(solver.searchRange(nums, target))
