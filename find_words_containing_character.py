class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        # Variables Initialization
        array = []
        idx = 0

        # Loops through the @words list checking whether character @x exist in a word and store it's index
        # in the array
        while idx < len(words):
            if x in words[idx]:
                array.append(idx)
            idx += 1

        # Return array of indices representing the words that contain the character x
        return array
