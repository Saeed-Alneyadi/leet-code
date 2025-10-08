class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Variables Initialization
        ans = 0

        # Loops through each number in @nums
        for num in nums:
            # Logically you would find the number divisble by 3 in the range of [num - 2, num + 2]
            if (num+1) % 3 == 0:
                num += 1
                ans += 1
            elif (num-1) % 3 == 0:
                num -= 1
                ans += 1
            elif (num+2) % 3 == 0:
                num += 2
                ans += 2
            elif (num-2) % 3 == 0:
                num -= 2
                ans += 2

        # Return @ans with the minimum number of operations to make all elements of nums divisble by 3
        return ans
