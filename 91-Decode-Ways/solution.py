import collections
import pdb

class Solution:
    def numDecodings(self, s: str) -> int:
        memoTable = collections.defaultdict(lambda: 0)
        self.recurse(s, 0, memoTable)
        return memoTable[0]

    
    """
    A recursion where we always look at the leading number and we pop it off and then
    continue down the chain. However, the numbers 10-26 are also valid.

    Base cases:
        1)  We have a valid value in the memo
        2)  We have reached the end of the string
    
    There are therefore 2 primary cases we have to look out for, and a special case:

    Case 1:
    The number is 1
        This means that there are 2 possibilities that we need to explore. In one case,
        we simply remove the number 1 and continue with that.

        In the other case, we have to remove 1 and the next number (essentially treat it as
        11 to 19), because these numbers are valid as well.

    Case 2:
    The number is 2:
        Again 2 possibilities. We simply remove 2.

        If the number after 2 is 0-6, we can remove it as well. (20 - 26 are valid)

    Case 3:
    The number is 0:
        This happens if we have "20", and remove the 2. This is invalid and we need to cut
        it out. Therefore, we return 0.
    """
    def recurse(self, inputString, pointer, memo):
        if memo[pointer] != 0:
            return memo[pointer]

        if pointer == len(inputString):
            return 1


        # Case 1
        if inputString[pointer] == "1" and pointer <= (len(inputString) - 2):
            memo[pointer] += self.recurse(inputString, pointer + 2, memo)
            memo[pointer] += self.recurse(inputString, pointer + 1, memo)
        # Case 2
        elif inputString[pointer] == "2" and pointer <= (len(inputString) - 2):
            if int(inputString[pointer + 1]) < 7:
                memo[pointer] += self.recurse(inputString, pointer + 2, memo)

            memo[pointer] += self.recurse(inputString, pointer + 1, memo)
        # Case 3
        elif inputString[pointer] == "0":
            return 0

        # Standard case
        else:
            memo[pointer] = self.recurse(inputString, pointer + 1, memo)

        return memo[pointer]

testStr = "20"
solver = Solution()
print(solver.numDecodings(testStr))
