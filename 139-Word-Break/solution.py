import collections
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        memo = collections.defaultdict(lambda: -1)
        realDict = collections.defaultdict(lambda: False)
        for word in wordDict:
            realDict[word] = True
        return self.recurse(s, realDict, 0, memo)

    """
    recurse
    We go through the current string and see what words fit in at the beginning. I.e. our
    dictionary has: [cat, cats, ...]
    Our word is: "catsanddogs"
    We need to consider breaking it doing both:
    cat // sanddogs
    cats // anddogs

    For sanddogs and anddogs, we save the pointer location, and memo the solution
    """
    def recurse(self, inputString, wordDict, pointer, memo):
        if memo[pointer] != -1:
            return memo[pointer]
        if pointer >= len(inputString):
            return True
        currAnswer = False
        for movingPointer in range(pointer, len(inputString) + 1):
            if (wordDict[inputString[pointer : movingPointer]]):
                currAnswer = currAnswer or self.recurse(inputString, wordDict, movingPointer, memo)
        memo[pointer] = currAnswer
        return currAnswer
