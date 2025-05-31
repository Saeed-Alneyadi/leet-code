class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        only_letters = re.sub(r'[^A-Za-z0-9]', '', s).lower()

        if only_letters == only_letters[::-1]:
            return True
        else:
            return False
 
