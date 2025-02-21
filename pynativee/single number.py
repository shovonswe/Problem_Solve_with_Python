class Solution:
    def singleNumber(self, nums):
        result = 0
        for i in nums:
          result ^= i
        return result  
nums = [3,3,1,4,5,4,5]
Solution = Solution()
print(Solution.singleNumber(nums))