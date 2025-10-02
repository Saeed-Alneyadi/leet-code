class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Multiply each index in the 1-indexed string with position of the character in the reversed alphabet, and return the sum of all results
        return sum((idx + 1) * (123 - ord(ch)) for idx, ch in enumerate(s))
