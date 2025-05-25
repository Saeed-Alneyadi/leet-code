class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        idx = x
        n = x

        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            while True:
                root = 0.5 * (idx + n / idx)
                if abs(root - idx) < 1e-6:
                    break
                idx = root

            return int(root)
