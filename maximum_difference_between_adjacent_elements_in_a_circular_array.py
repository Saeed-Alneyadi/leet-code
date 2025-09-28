class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Variables Initialization
        diff = []
        curr = nums[0]

        # Calculates the difference between all adjacent elements in @nums except adjacent 
        # elements of first and last element and add them to @diff
        for num in nums[1:]:
            diff.append(abs(num - curr))
            curr = num

        # Calculates the difference between the first and last element and add to @diff
        diff.append(abs(nums[len(nums) - 1] - nums[0]))

        # Return the maximum difference
        return max(diff)
