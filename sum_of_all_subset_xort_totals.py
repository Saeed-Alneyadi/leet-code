from itertools import chain, combinations

class Solution(object):
    @staticmethod
    def power_set(iterable):
        s = list(iterable)
        return [list(c) for r in range(len(s)+1) for c in combinations(s, r)]

    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialization
        sums = 0
        all_subsets = Solution.power_set(nums)

        # Loops through subsets to get XOR total
        for subset in all_subsets:
            # XOR total initialization
            xor = 0

            # Loops thorugh susbet instance to calculate XOR total for each subsets
            for instance in subset:
                xor = xor ^ instance
            
            # Add current subset XOR total to the whole sum
            sums += xor

        return sums
