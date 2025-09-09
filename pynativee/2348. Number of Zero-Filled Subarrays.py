class Solution:
    def zeroFilledSubarray(self, nums):
                    
       
            count = 0
            zero_count = 0
            for i in  nums:
              if i == 0:
                   zero_count += 1
                   count += zero_count
              else:
                   zero_count = 0      
            return count       
             

nums =[3,0,0,5,0,0,6,3]
sol = Solution()                  
print(sol.zeroFilledSubarray(nums))                  

 
      
