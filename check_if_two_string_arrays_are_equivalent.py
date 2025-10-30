class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        # Merge each strings array into its own string @word1 and @word2,
        # check whether the two words are equal and return based on that
        if "".join(word1) == "".join(word2):
            return True
        else:
            return False
