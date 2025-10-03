class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Transforming @n to list of digits stored @digits
        digits = [digit for digit in str(n)]

        # Return the maximum product of any two digits in @digits
        return max([int(d1) * int(d2) for idx1, d1 in enumerate(digits) for idx2, d2 in enumerate(digits) if idx1 != idx2])
