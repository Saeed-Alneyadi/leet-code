class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # Varaible Initialization
        i = 0

        # Remove last element and insert it at index @i
        while i < len(s):
            s.insert(i,s.pop(len(s) - 1))
            i += 1
