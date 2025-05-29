class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        elif n == 1:
            return True
        else:
            value_1 = math.log(n) / math.log(2)
            value_2 = int(value_1)
            if abs(value_1 - value_2) < 1e-14:
                print("here")
                return True
            else:
                return False
