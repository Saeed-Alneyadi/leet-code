class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        # Split @date into a list of year, month, and day which is stored in @date_list
        date_list = date.split("-")

        # Convert the unicode elements to integers
        date_list = [int(string) for string in date_list]

        # Return the binary representation of @date
        return bin(date_list[0])[2:] + "-" + bin(date_list[1])[2:] + "-" + bin(date_list[2])[2:]
