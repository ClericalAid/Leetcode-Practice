import collections

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = collections.defaultdict(lambda: -1)
        p1 = len(word1) - 1
        p2 = len(word2) - 1
        return self.recurse(memo, word1, word2, p1, p2)

    """
    Recursion where we cut characters off the string as we go down the chain. Instead of 
    actually cutting characters though, it is better to use pointers. There is no good way to 
    pop letters out if I recall correctly (or it exceeded the time limit on LeetCode)

    Base cases:

    Case 1:
    The letters at the end are the same. We can pop them off and go down the chain. This oepration
    does not cost a "move". It does not increase the distance at all.

    Case 2:
    One word is empty
        The amount of operations is the length of the word leftover. This is because we are doing
        X amount of inserts or deletes.

    Case 3:
    Letters at the end are different. All of these operations increase the "edit distance"

        a)
        We choose to delete the letter
        We proceed down the chain with one string being one character shorter (the character
        got deleted)

        b)
        We insert a letter to match
        We proceed down the recursion chain, but this time there is one string being shorter,
        and this string is the one where the character was NOT inserted. This happens because
        we insert a character to one string to force a match. This takes us back to "Case 1".
        And if the letters match, we pop them off and go down the chain. Therefore, inserting
        a character to one word is like deleting it from the other.
        

        c)
        We transform the current letter to match
        We proceed down the recursion chain but both strings get cut by 1 character. Again,
        this is like "Case 1" where there are matching characters. So we get to cut each string
        by 1.
    """
    def recurse(self, memo, word1, word2, ptr1, ptr2):
        if memo[(ptr1, ptr2)] != -1:
            return memo[(ptr1, ptr2)]

        if ptr1 == -1:
            return ptr2 + 1
        if ptr2 == -1:
            return ptr1 + 1

        # Case 1:
        if word1[ptr1] == word2[ptr2]:
            memo[(ptr1, ptr2)] = self.recurse(memo, word1, word2, ptr1 - 1, ptr2 - 1)

        # Case 2:
        else:
            # a)
            deleteLetter = self.recurse(memo, word1, word2, ptr1 - 1, ptr2) + 1
            # b)
            insertLetter = self.recurse(memo, word1, word2, ptr1, ptr2 - 1) + 1
            # c)
            transformLetter = self.recurse(memo, word1, word2, ptr1 - 1, ptr2 - 1) + 1

            memo[(ptr1, ptr2)] = min(deleteLetter, insertLetter, transformLetter)
        return memo[(ptr1, ptr2)]

str1 = "horse"
str2 = "ros"
solver = Solution()
print(solver.minDistance(str1, str2))
