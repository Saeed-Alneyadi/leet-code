class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Variables Initialization
        inc = True
        sen = s.split()
        nums = []
        idx = 0

        # Loops through the words and check if it is a number or not, add it if it is
        # Checks everytime it adds a number to the @nums list whether the list is in ascending order
        for word in sen:
            if word.isdigit():
                nums.append(int(word))
                idx += 1

                if len(nums) > 1 and nums[idx - 2] >= nums[idx - 1]:
                    inc = False
        
        # Return @nums number list in ascending order
        return inc
