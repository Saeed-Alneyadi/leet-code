class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Variable Initialization
        ans = list(s)
        i, j = 0, len(s) - 1

        # Swipe the vowels inside the @s string
        while i < j:
            if ans[i] in "aeiouAEIOU":
                while not ans[j] in "aeiouAEIOU":
                    j -= 1

                temp = ans[j]
                ans[j] = ans[i]
                ans[i] = temp

                j -= 1

            i += 1

        # Connect all letter with reversed vowels in one string and return it
        return "".join(ans)
