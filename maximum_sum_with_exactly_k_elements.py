import numpy as np

class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Variable Initialization
        answer = 0

        # Loops @k times
        for i in range(k):
            idx = np.argmax(nums) # Gets the index of the maximum value in @nums
            answer += nums[idx] # Increment @answer with maximum value
            nums[idx] += 1 # Increment the maximum value in @nums

        # Return @answer
        return answer
