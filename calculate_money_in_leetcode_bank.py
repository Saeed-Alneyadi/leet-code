class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Variables Initialization
        add, start, ans = 0, 0, 0
        
        # Loops #n times
        for idx in range(n):
            # If it is Monday...
            if idx % 7 == 0:
                start += 1 # Increment the starting amount of money every Monday
                add = 0 # Reset the addition of money to zero

            ans += add + start # Putting the amount of money needed to be added on current day

            add += 1 # Increment the amount of money need to be added

        # Return @ans with the total money left in the bank
        return ans
