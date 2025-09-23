class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        # Variable Initializtion
        sum = 0
        salary.remove(max(salary))
        salary.remove(min(salary))

        # Calculates the sum of @salary array
        for sal in salary: sum += sal

        # Return the average of the @salary array
        return float(sum)/float(len(salary))
