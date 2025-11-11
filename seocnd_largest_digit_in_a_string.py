class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Variable Initialization
        high = -1
        sec_high = -1

        # Checks every digit in @s and see which is the heighest
        for digit in s:
            if digit.isdigit() and digit > high:
                sec_high = high
                high = digit
            elif digit.isdigit() and digit > sec_high and digit < high:
                sec_high = digit

        # Return @sec_high as integer which is the second highest number in @s
        return int(sec_high)
