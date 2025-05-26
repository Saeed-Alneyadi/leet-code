class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        current = num
        while True:
            sum = 0
            num_str = str(current)
            # print(f"Current number: {current}, Digits: {num_str}")
            for digit in num_str:
                sum += int(digit)

            current = sum
            # print(f"Sum of digits: {sum}")

            if len(str(current)) <= 1:
                break

        return current
