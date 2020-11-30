import collections

class Solution:
    """
    isAnagram
    input:
        s - a string which we are comparing to string 't'
        t - another string, which we are comparing to string 's'
    Theory:
    If 's' and 't' are anagrams, then they would have matching letter counts. We can check
    this by using a defualt dictionary, and counting letters in one string, then subtracting
    them in another. The ending dictionary should have all keys returning a value of 0

    Steps for success:
    1)  Count the letters in string 's' and put them in a defaultdict
    2)  Go through each letter in string 't', and subtract them from our defaultdict
    3)  Check that all keys have a value of 0
    """
    def isAnagram(self, s: str, t: str) -> bool:
        letterCount = collections.defaultdict(lambda: 0)
        for letter in s:
            letterCount[letter] += 1
        for letter in t:
            letterCount[letter] -= 1
        for key in letterCount:
            if letterCount[key] != 0:
                return False
        return True
