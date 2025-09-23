class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        # Variables Initialization
        date_string = date.split()
        day = ''.join(c for c in date_string[0] if c.isdigit())
        dictionary = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        month = str(dictionary.index(date_string[1]) + 1)

        # Fixing the @month and @day formats
        if int(month) < 10:
            month = "0" + month

        if int(day) < 10:
            day = "0" + day

        # Return the date in the proper format
        return str(date_string[2]) + "-" + month + "-" + day
