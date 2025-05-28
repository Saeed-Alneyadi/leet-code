class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        tokens = s.split()

        new_tokens = []
        idx = 0
        while idx < len(tokens):
            token = tokens[idx][::-1]
            new_tokens.append(token)
            idx += 1

        return ' '.join(new_tokens)
