class Solution:
    def findDisappearedNumbers(self, nums):
        # Use the input array to mark visited numbers
        for num in nums:
            
            index = abs(num) - 1  # Convert the number to index
            if nums[index] > 0:  
                nums[index] = -nums[index]

        # Collect the indices where the value is positive 
        result = []
        for i in range(len(nums)):
            if nums[i] > 0: 
                result.append(i + 1) 
        return result

