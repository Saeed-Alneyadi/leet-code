class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        # Variable Initialization
        time = 0

        # Loops through the tickets list
        while len(tickets) > 0:
            # print(tickets)
            tickets[0] -= 1

            time += 1
            temp = tickets.pop(0)
            
            if temp > 0:
                tickets.append(temp)
                if k == 0:
                    k = len(tickets) - 1
                else:
                    k -= 1
            elif k > 0:
                k -= 1
            else:
                break

            # print(str(tickets) + "\n")

        # Return @time
        return time
