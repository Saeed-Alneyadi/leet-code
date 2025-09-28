class Solution(object):
    def hasMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Variable Initialization
        result = False
        starIdx = p.index("*")

        # Cuts @r into @l and @r where @l consist of the left string of the astrisk and @r is the other side
        l = p[0:starIdx]
        r = p[starIdx + 1:]
        # print(l)
        # print(r)

        # Checks @l is in @s and @r is in @s and the whether the index of @l is less than @r, if so, result set to True
        if (l in s or l == "") and (r in s or r == "") and s.find(l) + len(l) <= s.rfind(r):
            result = True
        
        # Return @result
        return result
