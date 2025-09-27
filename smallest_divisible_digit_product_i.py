class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        # Variable Initialization
        result = n

        while True:
            # Variable Initialization
            product = 1
            
            # Calculate digit products of @result
            for digit in str(result):
                product *= int(digit)

            # Check whether the product of the digits is divisible by @t, break from the loop if so
            if product % t == 0:
                break
            
            # Move on to the number greater than current @result
            result += 1

        # Return the smallest number greater than or equal to n such that the product of its digits is divisible by @t
        return result
