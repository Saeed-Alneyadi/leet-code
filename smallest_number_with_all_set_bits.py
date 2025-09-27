class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Variables Initialization
        result = n

        # Checks whether there is zero in the @result binary representation for n and greater 
        # values until it finds one
        while True:
            if str(bin(result))[2:].count("0") > 0:
                result += 1
            else:
                break

        # Return @result with smallest number x greater than or equal to n, such that 
        # the binary representation of x contains only set bits
        return result
