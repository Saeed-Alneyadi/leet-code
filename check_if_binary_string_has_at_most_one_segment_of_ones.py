class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Split the @s string in to 1 segments and see if there is less than 2 and return @True based on that
        return len([str(ch) for ch in s.split("0") if str(ch) != ""]) < 2
