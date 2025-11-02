class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        # Variables Initializations
        list1, list2 = list(word1), list(word2)
        ans = []
        idx = 0

        # Generates an alternating string between word1 ans word2
        while len(list1) > 0 and len(list2) > 0:
            if idx % 2 == 0:
                ans.append(list1.pop(0))
            else:
                ans.append(list2.pop(0))

            idx += 1 # Incrementing @idx
        
        # Add the remianing characters of either @word1 or @word2
        if len(list1) > 0:
            return "".join(ans + list1)
        else:
            return "".join(ans + list2)
