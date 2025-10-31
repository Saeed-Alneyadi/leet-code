class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        # Create the @balls list where it contains the sums of numbers' digits
        balls = [sum(map(int, str(lowLimit + i))) for i in range(highLimit - lowLimit + 1)]

        # Calculate the @counts of balls in each box
        counts = [balls.count(num) for num in set(balls)]

        # Return the maximum of @counts which corresponds the number of balls in the box with the most balls
        return max(counts)
