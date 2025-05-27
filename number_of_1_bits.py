class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Initialization of Variables
        binary = bin(n)[2:]
        sum = 0

        # For loop that loops throught the digit of binary representation of the number
        for idx, digit in enumerate(binary):
            if digit == '1':
                sum += 1

        return sum
