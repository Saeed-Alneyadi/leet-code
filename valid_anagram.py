class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # Check if two words have same characters and number of characters
        return Counter(s) == Counter(t)
