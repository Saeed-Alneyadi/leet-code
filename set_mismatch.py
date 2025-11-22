class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # Variables Initialization
        dupp = [num for num in set(nums) if nums.count(num) > 1][0]
        miss = -1 # Miss varaiable
        nums.sort() # Sorting @nums
        nums.remove(dupp) # Removing duplicates so indices matches with value
        i = 1 # Keep the track of for loop index varaible to access it after for loop

        # Loops through the sorted @nums where if the index doesn't match the value, the @miss varaible will be assigned to it
        for i in range(1,len(nums) + 1):
            if i != nums[i-1]:
                miss = i
                break

        # If the miss value hasn't found by the for loop, index variable increment by one is assigned to @miss
        if miss == -1:
            miss = i + 1

        # Return the asked array with the two duplicate and missing numbers
        return [dupp, miss]
