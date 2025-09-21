class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        # Variables Initialization
        result = time
        unknowns = []

        # Loops through the @time input and check for question mark
        for idx, digit in enumerate(time):
            if digit == '?':
                unknowns.append(idx)

        # Loops through @unknown and change the time blank digits to the maximum possible digit in that spot
        idx = 0
        while idx < len(unknowns):
            if unknowns[idx] == 0:
                # print(result)
                result = result[:idx + 1] + '2' + result[idx + 2:]
                # print(result)
            elif unknowns[idx] == 1:
                # print(result)
                result = result[:idx + 1] + '3' + result[idx + 2:]
                # print(result)
            elif unknowns[idx] == 2:
                # print(result)
                result = result[:idx + 2] + '5' + result[idx + 3:]
                # print(result)
            elif unknowns[idx] == 3:
                # print(result)
                result = result[:idx + 2] + '9' + result[idx + 3:]
                # print(result)
            idx += 1

        # Return @result with new maxed digits
        return result
