class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Variable Initialization
        inc = True
        dec = True

        # Checks whether the array @nums is monotonic increasing
        prev = nums[0]
        for i in range(len(nums) - 1):
            print(str(i) + " " + str(nums[i]))
            if prev > nums[i+1]:
                inc = False
                break
            prev = nums[i+1]

        # Checks whether the array @nums is monotonic decreasing
        prev = nums[0]
        for i in range(len(nums) - 1):
            if prev < nums[i+1]:
                dec = False
                break
            prev = nums[i+1]

        # Return the XOR of @inc and @dec
        return inc or dec
