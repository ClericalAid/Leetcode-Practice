import collections

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = collections.defaultdict(lambda: -1)
        return self.recurse(text1, text2, 0, 0, memo)

    """
    recurse
    Trivial base cases:
    - Solution exists in the memo
    - pointer has escaped the string

    A recursion where we compare 2 letters and make a choice:
    1)  Letters are the same
        Pop them both out
    2)  Letters are different
        a)  Eliminate the mismatched letter from text1
        b)  Eliminate the mismatched letter from text2
    Perform recursion on the shortened strings
    """
    def recurse(self, text1, text2, pointer1, pointer2, memo):
        if (pointer1 >= len(text1)):
            return 0
        if (pointer2 >= len(text2)):
            return 0

        if (memo[(pointer1, pointer2)] != -1):
            return memo[(pointer1, pointer2)]

        if (text1[pointer1] == text2[pointer2]):
            memo[(pointer1, pointer2)] = self.recurse(text1, text2, pointer1 + 1, pointer2 + 1, memo) + 1

        elif (text1[pointer1] != text2[pointer2]):
            memo[(pointer1, pointer2)] = max(self.recurse(text1, text2, pointer1 + 1, pointer2, memo), self.recurse(text1, text2, pointer1, pointer2 + 1, memo))
        return memo[(pointer1, pointer2)]
