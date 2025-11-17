class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        # Variables Initializations
        count = nums.count(target)
        idx = 0
        curr = 0
        indices = []

        # Calculate the @abs(curr - start) for element that is equal to @target
        while idx < count:
            if curr < len(nums):
                curr = nums.index(target, curr, len(nums)) # Find the index of the target in order
            else:
                break # Break if end of @nums is reached
            
            indices.append(abs(curr - start)) # Append @target element @abs(curr - start value to @indices
            curr += 1 # Incrment @curr
            idx += 1 # Incrment @idx

        # Return the minimum of @indices which is the minimized @abs(i - start)
        return min(indices)
