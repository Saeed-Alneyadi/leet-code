class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        # Find the words that appeared once in @words1 and @words2 and add them to @appeared
        appeared = [str(word) for word in words1 if word in words2 and words1.count(word) <= 1 and words2.count(word) <= 1]

        # Return the number of those specific words
        return len(appeared)
