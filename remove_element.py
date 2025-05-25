class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ini_len = len(nums)
        idx = 0
        k = 0
        while idx < len(nums):
            if nums[idx] == val:
                nums.remove(val)
                k += 1
            else:
                idx += 1

        return ini_len - k
