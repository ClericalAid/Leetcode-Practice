import collections

class Solution:
    """
    Use two pointers to the string. The first pointer traverses the string until a duplicate
    character is found. When a duplicate character is found, the second pointer begins traversing
    the string and removes characters from the counter.

    In this case, 'i' and 'j' are the two pointers, with 'i' traversing the string first.
    'j' starts at -1 because the moment it sees a character said character is removed. It's a bit
    backwards
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        charCounter = collections.defaultdict(lambda: 0)
        i = 0
        j = -1
        longestSS = 0
        for i in range(len(s)):
            charCounter[s[i]] += 1
            while charCounter[s[i]] > 1:
                j += 1
                charCounter[s[j]] -= 1
            length = i - j
            if length > longestSS:
                longestSS = length
        return longestSS


sampleInput = "abcabcbb"
solver = Solution()
print(solver.lengthOfLongestSubstring(sampleInput))
            


