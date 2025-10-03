class Solution(object):
    def minDeletion(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Variables Initialization
        answer = 0
        chs = list({str(ch) for ch in s})
        print(chs)
        counts = [s.count(ch) for ch in chs]
        print(counts)

        # Loops until the number of distinct character in @s is equal to @k
        while len(chs) > k:
            min_counts_idx = counts.index(min(counts))
            ch = chs[min_counts_idx] # Getting the character @ch with minimum count in @counts
            counts.pop(min_counts_idx) # Poping the character @ch count in @counts
            chs.remove(ch) # Removing the character @ch in @chs
            answer += s.count(ch) # Incrementing @answer with counts @ch in @s
            s.replace(ch,"") # Remove every instance of @ch in @s

        # Return @answer which is the minimum number of deletions to get @s of @k distinct characters
        return answer
