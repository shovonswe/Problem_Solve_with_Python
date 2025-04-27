class Solution:
    def pivotIndex(self,nums):
        total_sum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]
            if right_sum == left_sum:
                return i
            left_sum += nums[i]
        return -1        
Solution = Solution()
nums = [1,7,3,6,5,6]
print(Solution.pivotIndex(nums))    