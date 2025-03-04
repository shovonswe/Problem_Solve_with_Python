class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0
        current_count = 0
        for i  in nums:
            if i == 1:
                current_count += 1
            else:
                max_count = max(max_count, current_count)
                current_count = 0
        return max (current_count,max_count)        
Solution = Solution()
nums = [1,1,0,0,4,1,1,1,9]
print(Solution.findMaxConsecutiveOnes(nums))