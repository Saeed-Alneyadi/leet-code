class Solution(object):
    def distanceTraveled(self, mainTank, additionalTank):
        """
        :type mainTank: int
        :type additionalTank: int
        :rtype: int
        """
        # Variable Initialization
        distance = 0
        used = 0

        # While loops keep running until @mainTank reach zero
        while mainTank > 0:
            # Decrementing @mainTank and incrementing both @used and @distance by 1 and 10 respectively
            mainTank -= 1
            used += 1
            distance += 10

            # If @used is more than 5 and there is fuel in @additionalTank, 1L fuel transfer from @additionalTank to @mainTank
            # @used become zero
            if used >= 5 and additionalTank > 0:
                additionalTank -= 1
                mainTank += 1
                used = 0

        # Return the maximum distance traveled
        return distance
