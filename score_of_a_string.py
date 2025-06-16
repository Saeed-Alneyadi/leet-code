class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Variable Initialization
        sum = 0

        # Calculate the absolute value of the difference between the
        # ASCII value of adjacent characters in @s
        for idx in range(len(s) - 1):
            sum += abs(ord(s[idx]) - ord(s[idx+1]))

        # Return the calculated @sum
        return sum
