class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Variable Initialization
        array = [0,1,1]

        # If n is equal to zero, zero is returned
        if n == 0:
            return 0

        # Loops in the range of n - 2 while appending the tribonacci to the @array
        for i in range(n - 2):
            array.append(array[i] + array[i + 1] + array[i + 2])

        # print(array)

        # Return the last element in @array since loop stops at calculating T_n
        return array[len(array) - 1]
