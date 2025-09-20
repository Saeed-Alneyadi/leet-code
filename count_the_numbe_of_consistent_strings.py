class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        # Get the words that only contains characters in @allowed
        consistant = [word for word in words if all(ch in allowed for ch in word)]

        # Return the number of these kind of words
        return len(consistant)
