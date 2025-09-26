class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Find the indices of the "AB" and "CD" substrings in @s
        idx1 = s.find("AB")
        idx2 = s.find("CD")

        # Keeps removing every "AB" and "CD" in string @s
        while idx1 != -1 or idx2 != -1:
            if idx1 != -1:
                s = s[0:idx1] + s[idx1 + 2:]
            elif idx2 != -1:
                s = s[0:idx2] + s[idx2 + 2:]

            # Find the indices of the "AB" and "CD" substrings in @s
            idx1 = s.find("AB")
            idx2 = s.find("CD")

        # Return the length of the minimum possible length of the resulting string which is @s
        return len(s)
