class Solution(object):
    def minCosts(self, cost):
        """
        :type cost: List[int]
        :rtype: List[int]
        """
        # Moves through @cost array to 
        answer = [cost[0]]
        for num in cost[1:]:
            # Stores last element appended in the @answer array
            prev =  answer[len(answer) - 1]

            # Checks if the last element appended in the @answer array is larger 
            # than @num which is the current element that we are inspecting in @cost
            if prev >= num:
                answer.append(num) # @num appended to @answer
            else:
                answer.append(prev) # @prev value is appended to @answer

        # Return an array @answer of size n, where answer[i] is the minimum total cost to reach each position i in the line
        return answer
