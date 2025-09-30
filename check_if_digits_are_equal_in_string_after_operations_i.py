class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Calculate two consecuative digits sum modulo 10 and store the results ordered in one new @s string
        while len(s) > 2:
            s = "".join([str((int(s[idx]) + int(s[idx + 1])) % 10) for idx in range(len(s) - 1)])

        # If the final two digits in @s are the same, return @True, otherwise @False
        return s[0] == s[1]
