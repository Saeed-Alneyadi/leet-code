class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Uses @ord() and @chr() to replace every digit in @s with a character before @s shifted by @s[i]
        for i in range(1,len(s), 2):
            s = s[0:i] + chr(ord(s[i-1]) + int(s[i])) + s[i+1:]

        # Return the new @s string
        return s
