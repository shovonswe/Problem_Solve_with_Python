from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
       
        nums = list(map(str, nums))
        def compare(a, b):
            if a + b > b + a:
                return -1  
            elif a + b < b + a:
                return 1   
            else:
                return 0
    
        nums.sort(key=cmp_to_key(compare))
        result = ''.join(nums)
        return '0' if result[0] == '0' else result
nums = [3,30,34,5,9]
sol = Solution()
print(sol.largestNumber(nums))