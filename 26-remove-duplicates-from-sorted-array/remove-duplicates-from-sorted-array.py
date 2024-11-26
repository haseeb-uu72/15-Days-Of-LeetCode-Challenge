class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0  #list empty= return 0
        
        # i tracks the position to insert the next unique number
        i = 1  # Start fromsecond element
        
        # Start from the second element and check for duplicates
        for j in range(1, len(nums)):
            if nums[j] != nums[j - 1]:  #a unique element is found
                nums[i] = nums[j]  # Place it at i-th index
                i += 1  # Move for the next unique element
        
        # i will be the count of unique elements
        return i
