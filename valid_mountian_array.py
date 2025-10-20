class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) >= 3:
            # Varaibles Initialization
            inc = True
            didInc = False
            dec = False
            ans = True
            prev = arr[0]

            # Checks whether the array increasing and then decreasing if not @False will be returned
            for num in arr[1:]:
                if inc:
                    if num > prev:
                        inc = True
                        didInc = True
                    else:
                        inc = False

                if not inc:
                    if not num < prev:
                        ans = False
                        break
                    else:
                        dec = True

                prev = num

            # Return the result of whether the array is increasing and then decreasing
            return ans and dec and didInc
        else:
            # Return @False if the array length is length of it is less than 3 since it wouldn't be a mountain
            return False
