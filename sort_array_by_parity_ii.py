class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Variable Initalization
        evens = []
        odds = []
        ans = []

        # Loops through the @nums array where it append even number to @evens and odds number to @odds
        for num in nums:
            if num % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)

        # print(evens) # DEBUG
        # print(odds) # DEBUG

        idx = 0
        while len(evens) > 0 or len(odds) > 0:
            if idx % 2 == 0:
                ans.append(evens.pop(0))
            else:
                ans.append(odds.pop(0))

            idx += 1
        
        # Return @ans where evens are in evens indices and odds in odds indices
        return ans
