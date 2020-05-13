import collections
class Solution:
    """
    I was unable to find the DP/ recursive approach at first, so I had to look it up online. All
    the solutions I saw used the dynamic programming approach from the bottom up. In order to
    learn as much as I can, I tried to take the standard DP approach and turn it into a recursive
    solution.

    This solution should run in O(n^2), but times out.
    """
    def longestPalindrome(self, s: str) -> str:
        solutionSaver = collections.defaultdict(lambda: 0)
        self.recurse(s, 0, len(s)-1, solutionSaver)
        longestPal = max(solutionSaver, key=solutionSaver.get)
        return s[longestPal[0] : longestPal[1] + 1]

    """
    Perform a recursion on our string. To do this, we check the following:

    1)
    The base case occurs when the string is of length 1 or 2. 
        If the length is 1, we have a palindrome of length 1
        If the length is 2, we either have a palindrome of length 2 or no palindrome
        To handle this case, if the "beginning" is greater than the "end", then we return
        0. This means that we overshot because we found two matching characters earlier

    2)
    If the first and last characters of our substring match:
        Check if the inner string is a palindrome recursively 

    Otherwise:
        Knock out the first letter:
            Recurse on that substring
        Knock out the last letter:
            Recurse on that substring

    Our memo needs to tell us three things:
    1) Did we explore this substring before? (default value)
    2) Is this substring a palindrome? (return its length)
    3) Was this substring found to not be a palindrome? (special value)
    """

    def recurse(self, s, beginning, end, memo):
        if memo[(beginning, end)] != 0:
            return memo[(beginning, end)]

        # 1)
        if beginning > end:
            return 0
        elif beginning == end:
            memo[(beginning, end)] = 1

        # 2)
        elif s[beginning] == s[end]:
            innerPalindrome = self.recurse(s, beginning + 1, end - 1, memo)
            if innerPalindrome == -1:
                memo[(beginning, end)] = -1
            else:
                memo[(beginning, end)] = 2 + innerPalindrome
        else:
            memo[(beginning, end)] = -1

        if memo[(beginning, end)] == -1:
            self.recurse(s, beginning + 1, end, memo)
            self.recurse(s, beginning, end - 1, memo)
        return memo[(beginning, end)]

sampleInput = "babadada"
solver = Solution()
print(solver.longestPalindrome(sampleInput))
