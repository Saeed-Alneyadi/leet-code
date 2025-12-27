class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # Variable Initialization
        n = 1
        ans = 0
        
        # This added to count the sum of the whole subarray in case if its length is odd
        if len(arr) % 2 == 1:
            ans = sum(arr)

        # Calculate the odd length subarrays sum
        while n < len(arr):
            # Varaibles Initialization
            i = 0

            # Add all the @n th sized subarrays sums to the total
            while i < len(arr) + 1 - n:
                # print(arr[i:i + n]) # DEBUG
                ans += sum(arr[i:i + n]) # Add the subarray sum to whole total which is @ans
                i += 1 # Increment @i to move on to the other subarray

            # Incrementing @n by two to ensure taking only odd length subarrays
            n += 2

        # Return @ans which contains the sum of all subarrays
        return ans
