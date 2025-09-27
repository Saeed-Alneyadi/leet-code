class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        # Variable Initialization
        word = "a"

        # Update @word with @new for every iteration where the @new is @word with characters shifted to the next character
        while len(word) <= k:
            new = "".join([chr(ord(ch) + 1) for ch in word])
            # print(word)
            # print(new)
            word = word + new

        # Return the kth character of the new @word
        return word[k - 1]
