class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        # Loops through every character in @word and replace it with space if it is not a digit
        for idx, ch in enumerate(word):
            if not ch.isdigit():
                word = word[0:idx] + " " + word[idx+1:] # Replace the current character with a space

        # Split word into a list and then strip zeros from the left of any element, count distinct element and return this count
        return len(set([ch.lstrip("0") for ch in word.split()]))
