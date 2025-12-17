class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        # Varaibles Initialization
        ans = []

        # Append element in the asked order where an element from the first half
        # followed by an element in the second half
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i + n])

        # Return @ans
        return ans
