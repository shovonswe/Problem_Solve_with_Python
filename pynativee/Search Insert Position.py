class Solution:
    def searchInsert(self, nums,target):
        for i in range(len(nums)):
            if(nums[i]  >= target):
                return i

        return len(nums)
nums = [1,3,5,6]
target = 7
sol = Solution()
print(sol.searchInsert(nums,target))