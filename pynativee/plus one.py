class Solution:
    def plusOne(self, nums):
        for i in range(len(nums)-1, -1, -1):  
            if nums[i] < 9: 
                nums[i] += 1
                return nums
            nums[i] = 0  
        
        
        return [1] + nums  

nums1 = [1, 2, 3]  
nums2 = [4, 3, 2, 1]  
nums3 = [9, 9, 9] 

sol = Solution()
print(sol.plusOne(nums1))
print(sol.plusOne(nums2))
print(sol.plusOne(nums3))
