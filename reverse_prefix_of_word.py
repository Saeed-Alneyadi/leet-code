class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        end = word.find(ch) # Gives the index of first @ch in @word

        if end == -1:
            return word # Return same @word if ch doesn't exist in @word
        else:
            return word[:end + 1][::-1] + word[end + 1:] # Return @word with the reversed substring
