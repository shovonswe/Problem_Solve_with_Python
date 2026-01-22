class Solution:
    def removeDuplicates(self, nums):
          if len(nums)<=2:
               return len(nums)
          s = 2
          for i in range(2,len(nums)):
            if nums[i] != nums[s-2]:
               nums[s] = nums[i]
               s += 1
          return s     


solution = Solution()        
nums = [1,1,1,2,2,3]
print(solution.removeDuplicates(nums))
        