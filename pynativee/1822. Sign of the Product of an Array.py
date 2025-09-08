class Solution:
    def arraySign(self, nums):
           ans = 1
           for i in nums:
                 ans *= i
           if ans>0:
             return 1
           if ans<0:
            return -1
           if ans == 0:
               return 0      
nums = [1,5,0,2,-3]
sol = Solution()
print(sol.arraySign(nums))