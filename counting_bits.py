class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # Count the number of ones for each binary respresentation of each number from 0 to n, inclusive
        return [bin(i)[2:].count("1") for i in range(n + 1)]
