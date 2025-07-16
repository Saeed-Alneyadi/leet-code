class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Do the intended operations until it gets only two digits
        while len(s) > 2:
            result = ""
            idx = 0
            while idx < len(s) - 1:
                num = (int(s[idx]) + int(s[idx + 1])) % 10
                result = result + str(num)
                idx += 1

            s = result

        # Checks whether the last two digits are equal which returns True otherwise False
        if s[len(s) - 2] == s[len(s) - 1]:
            return True
        else:
            return False
        
