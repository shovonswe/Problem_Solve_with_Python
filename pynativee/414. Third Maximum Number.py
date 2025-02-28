class Solution:
    def thirdMax(self, nums):

        nums = sorted(set(nums), reverse = True)
      
        return nums [2] if len(nums) >= 3 else  nums[0]
       
        

nums =[1,1,2]
Solution = Solution ()
print(Solution.thirdMax(nums))        