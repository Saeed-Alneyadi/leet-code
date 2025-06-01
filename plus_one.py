class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        idx = len(digits) - 1 # Start from the last digit
        digits[idx] += 1 # Increment the last digit by one

        # Handle carry over if the digit exceeds 9
        while digits[idx] > 9:
            digits[idx] = 0 # Set current digit to 0
            idx -= 1 # Move to the next digit to the left

            # If idx is negative, it means we have a carry that needs to be added
            # at the front of the list
            if idx < 0:
                digits.insert(0, 1)
                idx += 1
            else:
                digits[idx] += 1

        return digits # Retrun the modified list of digits
