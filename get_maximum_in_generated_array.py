class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Handle the case where @n is less than 2
        if n < 2:
            return n
        
        # Variable Initialization
        arr = [0,1]
        idx = 2

        # Build the required array
        while len(arr) < n + 1:
            if idx % 2 == 0:
                arr.append(arr[idx / 2])
            else:
                arr.append(arr[(idx - 1) / 2] + arr[((idx - 1) / 2) + 1])

            idx += 1

        # print(arr) # DEBUG
        return max(arr)
