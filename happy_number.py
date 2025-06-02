class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Variable Initializations
        current = str(n)
        i = 0

        # Loop until we reach "1" or exceed 30 iterations
        # (to prevent infinite loops)
        while current != "1":
            # Variables Initializations
            sum = 0
            idx = 0

            # Calculate the sum of squares of digits
            while idx < len(current):
                num = int(current[idx])
                sum += num * num
                idx += 1

            # Update current to the new sum
            current = str(sum)
            print(current)

            # Check if we have exceeded 30 iterations
            if i > 30:
                return False
                break

            # Increment the iteration counter
            i += 1

        # Return Statement
        return True
