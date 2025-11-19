class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Variable Initialization
        sentence = s.split()
        idx = 1
        i = 0
        ans = []

        # Walks out through @sentence list and append words in order to @ans
        while len(ans) < len(sentence):
            word = sentence[i % len(sentence)] # Store the current word with indec @i
            if int(word[len(word)-1]) == idx:
                ans.append(word[0:len(word) - 1]) # Append the word without its order number
                idx += 1 # Increment @idx which is sentence index 

            i += 1 # Increment @i which is loops counter

        # Return the new order sentence without numbers
        return " ".join(ans)
