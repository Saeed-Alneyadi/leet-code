class Solution(object):
    def vowelStrings(self, words, left, right):
        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """
        # Return the number of vowel strings words[i] where i belongs to the inclusive range [left, right]
        return len([word for word in words[left: right + 1] if word[0] in "aeiou" and word[len(word) - 1] in "aeiou"])
