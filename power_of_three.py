import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Check if n is a power of 3
        if n <= 0:
            return False # Return Statement
        elif n == 1:
            return True # Return Statement
        else:
            value_1 = round(math.log(n) / math.log(3), 13) # Calculate logarithm
            value_2 = int(value_1) # Convert to integer

            # Compare the rounded value with the integer value
            if abs(value_1 - value_2) < 1e-16:
                return True # Return Statement
            else:
                return False # Return Statement
        
