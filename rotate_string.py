class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        # Variables Initializations
        idx = 0

        # Search every rotation combination and check whether it matches the @goal
        while idx < len(s):
            if s[idx:] + s[:idx] == goal:
                return True # Return True since there is a string that matches @goal
            idx += 1

        return False # Return False since there is no string matches @goal
