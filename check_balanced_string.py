class Solution(object):
    def isBalanced(self, num):
        """
        :type num: str
        :rtype: bool
        """
        # Getting the odds sum and evens sum using sum function
        oddsSum = sum(int(digit) for idx, digit in enumerate(str(num)) if idx % 2 == 1)
        evensSum = sum(int(digit) for idx, digit in enumerate(str(num)) if idx % 2 == 0)
        # print(oddsSum)
        # print(evensSum)

        # Checks whether @oddsSum and @evensSum are equal, if so, true returned, otherwise, false
        return oddsSum == evensSum
