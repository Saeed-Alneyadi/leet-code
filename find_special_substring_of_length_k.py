class Solution(object):
    def hasSpecialSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        # Variable Initialization
        result = False
        sub = str(s[0])

        # Loops from second character in @sub where it extracts only k adjacent identical characters 
        # where characters before and after are different
        for ch in s[1:]:
            # Set @result to @True when @sub length is equal to @k and the character @ch, which is after the substing @sub,
            # is not in substring @sub
            if len(sub) == k and ch not in sub:
                result = True
                break
            # Ensure result set to @False and @sub to the current character @ch
            elif ch not in sub:
                result = False
                sub = ch
            # Concatenate the current @ch to the current substring @sub
            else:
                sub = sub + ch
        
        # Handle the case if @sub contains @k identical adjacent characters after the run of the loop where it return @True
        if len(sub) == k:
            return True
        # Hanlde the case if @s is the length of 1 and equal to @k where it return @True
        elif len(s) == k == 1:
            return True
        # If neither these cases happens, @result will be returned
        else:
            return result
