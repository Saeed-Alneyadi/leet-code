class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Variables Initialization
        array = [1, 1]
        i = 2

        # Calculate a whole array that consist of Fibonacci Sequence till number n
        while i < n:
            array.append(array[i-1] + array[i-2])
            i += 1

        # Return the asked Fibonacci number
        if n == 0:
            return 0
        else:
            return array[n - 1]
