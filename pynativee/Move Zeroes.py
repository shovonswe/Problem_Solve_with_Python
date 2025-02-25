class Solution:
    def moveZeroes(self, nums):
        lastNonZeroFoundAt = 0
        
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZeroFoundAt], nums[i] = nums[i], nums[lastNonZeroFoundAt]
                lastNonZeroFoundAt += 1
        return nums        
Solution = Solution ()
nums = [0,1,0,3,12]
print(Solution.moveZeroes(nums))        