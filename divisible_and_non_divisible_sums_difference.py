class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        # Gives the sum of all integers in the range [1, n] for @num1 and @num2,
        # but @num1 have elements not divisible by m while @num2 the opposite
        num1 = sum((element + 1) for element in range(n) if (element+1) % m != 0)
        num2 = sum((element + 1) for element in range(n) if (element+1) % m == 0)

        # Return the differeence between @num1 and @num2
        return num1 - num2
