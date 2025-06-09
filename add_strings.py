class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        # Convert strings to integers, sum them up, 
        # convert the sum to string and return it
        return str(int(num1) + int(num2))
