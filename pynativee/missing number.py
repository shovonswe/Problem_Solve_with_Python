class  Solution:
      def missingNumber(self, nums):
            expected_sum = 0
            for i in range (len(nums)+1):
                  expected_sum = expected_sum + i
            list_sum = sum(nums)
            return expected_sum - list_sum      
nums = [1,4,2,3,9,7,8,5,0]
Solution = Solution()    
print(Solution.missingNumber(nums))        
            