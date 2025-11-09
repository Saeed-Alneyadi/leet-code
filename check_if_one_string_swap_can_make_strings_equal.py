class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2) or set(s1) != set(s2) or any([s1.count(ch) != s2.count(ch) for ch in s1]):
            return False # Return @False if there lengths are different, characters or counts is different
        else:
            # Varaibles Initialization
            count = 0
            idx = 0

            # See how many swaps needed to make them equal
            while idx < len(s1):
                if s1[idx] != s2[idx]: # Checks if characters at @idx are not equal in both strings
                    s1.replace(s1[idx], s2[idx]) # Replace character at @idx in @s1 with character in @s2
                    count += 1 # Increment @count

                    # If there is more than 2, @False are returned
                    if count > 2:
                        return False

                # Increment @idx
                idx += 1
        
        # Return @True if there is no condition that tells that there is at most one string swap
        return True
