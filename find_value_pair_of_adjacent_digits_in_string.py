class Solution(object):
    def findValidPair(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Variable Initialization
        pair = [s[idx] + s[idx + 1] for idx in range(len(s) - 1) if int(s[idx]) != int(s[idx + 1]) and int(s[idx]) == s.count(s[idx]) and int(s[idx + 1]) == s.count(s[idx + 1])]

        # Return "" if there is no pair in @pair and @pair[0] if there is one
        if len(pair) > 0:
            return pair[0]
        else:
            return ""
