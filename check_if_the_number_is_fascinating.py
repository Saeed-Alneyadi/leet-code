class Solution(object):
    def isFascinating(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Constructing the resulting number that consist of the concatenation of n, 2*n, 3*n
        num = str(n) + str(2*n) + str(3*n)
        
        # Check the resulting number whether it contains all digits from 1 to 9
        return all(num.count(digit) == 1 for digit in "123456789")
