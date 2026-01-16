class Solution:
    def minimumDifference(self, nums,k):
        if len(nums) == 1:
            return 0
        ans = float("inf")
        nums.sort()
        for i in range(len(nums)-k+1):
            ans =min(ans,nums[i+k-1]-nums[i])
        return ans    
            
solution = Solution()
nums = [9,4,1,7]   
k = 2 
print(solution.minimumDifference(nums,k))           