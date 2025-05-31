class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n <= 0:
            return False
        if n == 1:
            return True
        else:
            num = math.log(n) / math.log(4)

            num = num - int(num)

            if num == 0:
                return True
            else:
                return False
