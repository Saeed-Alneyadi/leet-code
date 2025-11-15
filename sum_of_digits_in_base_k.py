class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # Varaibles Initialization
        sum = 0

        # Sum up all remainders of divison process of @n by @k until @n become zero
        while n != 0:
            sum += n % k
            n = n / k

        # Return @sum which coresponds to the sum of the digit of the new number of base @k
        return sum
