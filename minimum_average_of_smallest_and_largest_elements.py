class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        # @average list initialization
        averages = []

        for i in range(len(nums)/2):
            minElement = min(nums) # Get the minimum element in @nums
            nums.remove(minElement) # Remove the minimum element from @nums
            maxElement = max(nums) # Get the maximum element from @nums
            nums.remove(maxElement) # Remove the maximum element from @nums

            # Append the average of @minElement and @maxElement to @averages
            averages.append(float(minElement + maxElement)/2)

        # Get the minimum average among @averages elements
        return min(averages)
