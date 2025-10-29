class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Variable Initialization
        length = len(code)
        ans = [0 for num in code]

        # Handle the case where @k is greater than 0
        if k > 0:
            for idx1, num1 in enumerate(code):
                # Variable Initialization
                total = 0
                idx2 = 1

                # Calculates the specific @total
                while idx2 <= k:
                    total += code[(idx1 + idx2) % length]
                    idx2 += 1

                ans[idx1] = total # Add the calculated @total to @ans
        
        # Handle the case where @k is less than 0
        elif k < 0:
            for idx1, num1 in enumerate(code):
                # Variable Initialization
                total = 0
                idx2 = -1

                # Calculates the specific @total
                while idx2 >= k:
                    total += code[(idx1 + idx2) % length]
                    idx2 -= 1

                ans[idx1] = total # Add the calculated @total to @ans

        # Return the array @ans 
        return ans
