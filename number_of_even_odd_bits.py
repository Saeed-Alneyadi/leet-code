class Solution(object):
    def evenOddBit(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # Return the number of even and odd bits in array of [even_count, odd_count]
        return [len([i for i, num in enumerate(str(bin(n))[2:][::-1]) if num == "1" and i % 2 == 0]), len([i for i, num in enumerate(str(bin(n))[2:][::-1]) if num == "1" and i % 2 == 1])]
