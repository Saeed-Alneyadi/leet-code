class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        # Variable Initialization
        if len(sentence) < 26:
            return False

        # Check if all characters in @sentence exist at least once
        return all([ch in sentence.lower() for ch in "abcdefghijklmnopqrstuvwxyz"])
