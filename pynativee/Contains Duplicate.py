class Solution:
    def containsDuplicate(self, nums):
       seen = set()
       for i in nums:
           if i in seen:
               return True
           seen.add(i)
             
       return False

Solution = Solution()
print(Solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
print(Solution.containsDuplicate([1,2,3,4]))