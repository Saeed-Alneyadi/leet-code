class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Initialization
        idx1 = 0
        result = []
        substrings = []
        
        # Create substring that starts at each character of @s
        while idx1 < len(s):
            # Initialization
            substrings = []
            idx2 = idx1
            curr = s[idx2]

            # Keeps adding character to the substring util duplicate character encountered
            while True:
                if curr in substrings:
                    break
                else:
                    # Append the character @curr to the current substring #substring
                    substrings.append(curr)

                    # Increment to next character in s
                    idx2 += 1
                    
                    # Handle the case where end of string @s is reached and no more character there
                    if idx2 < len(s):
                        curr = s[idx2]
                    else:
                        break
            
            # Add the substring to the current list of substrings to pick the max later
            result.append("".join(substrings))

            # Incrementing to the next substring starting character
            idx1 += 1

        # Return zero if @s is empty substring otherwise it return the max length word in substrings list
        if s != "":
            return len(max(result, key=len))
        else:
            return 0
