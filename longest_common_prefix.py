class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Variables Initialization
        ans = ""
        idx = 0
        flag = False

        # Loops for every character in the first word in @strs
        while idx < len(strs[0]):
            ans = ans + strs[0][idx] # Add one character to the prefix string @ans
            idx += 1 # Increment @idx with one

            # Loops through every word in @strs and check whether the current prefix is common among them
            for word in strs:
                if not word.startswith(ans):
                    flag = True # Outer Loop Breaker Condition
                    ans = ans[:-1] # Strip last character in the prefix
                    break # Inner Loop Breaker
            
            # Outer Loop Breaker Condition
            if flag:
                break # Outer Loop Breaker

        # Return the common prefix
        return ans
