class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Conveting the numbers to integers, add them, convert result to binary, return proper string
        return str(bin(int(a, 2) + int(b, 2)))[2:]
