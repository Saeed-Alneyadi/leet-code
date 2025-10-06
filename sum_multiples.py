class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Return the sum of all numbers in the given range satisfying the constraint of [1,n]
        return sum([num for num in [item for item in range(n + 1)][1:] if num % 3 == 0 or num % 5 == 0 or num % 7 == 0])
