class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # Calculate the product of all element in @nums
        product = math.prod(nums)
        
        # Checks the sign for the product and return based on that
        if product > 0:
            return 1
        elif product < 0:
            return -1
        else:
            return 0
