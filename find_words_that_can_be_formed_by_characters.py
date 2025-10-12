from collections import Counter

class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        # Return the sum of lengths of all good strings in @words
        return sum([len(word) for word in words if not (Counter(word) - Counter(chars))])
