class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        # Checks whether @word contains a minimum of 3 characters
        isMin = (len(word) >= 3)

        # Checks whether @word contains only digits (0-9), and English 
        # letters (uppercase and lowercase)
        containsDigUpperLower = all(char.isalnum() for char in word)

        # Checks whether @word includes at least one vowel
        vowels = 'aeiouAEIOU'
        includesVowel = any(char in vowels for char in word)

        # Checks whether @word includes at least one consonant
        includesConsonant = any(char.isalpha() and char not in vowels for char in word)

        # Checks whether all conditions are met
        if isMin and containsDigUpperLower and includesVowel and includesConsonant:
            return True
        else:
            return False
