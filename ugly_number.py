class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Ugly numbers must be positive
        if n <= 0:
            return False
        
        # Divide n by 2, 3, and 5 as long as possible
        # This removes all instances of these allowed prime factors
        for p in [2, 3, 5]:
            while n % p == 0:
                n //= p # Divide n by p

        # If we're left with 1, then all prime factors were 2, 3, or 5
        return n == 1
