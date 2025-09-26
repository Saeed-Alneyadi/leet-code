class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        # Variables Initialization
        string = num
        idx = len(string) - 1

        # Keeps removing trailing zeros from @string until it counters a non-zero digit
        while idx > 0:
            if int(string[idx]) == 0:
                string = string[0:idx]
            else:
                break 
            
            idx -= 1

        # Return the new string number with no trailing zeros
        return string
