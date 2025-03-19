class Solution:
    def findMaxAverage(self, nums, k):
        
        current_sum = sum(nums[:k])
        max_sum = current_sum
        for i in range(k,len(nums)):
            current_sum += nums[i] - nums[i-k]
            max_sum = max(max_sum,current_sum)

        return max_sum/k
        
Solution = Solution()
nums = [1,12,-5,-6,50,3]
k = 4
print(Solution.findMaxAverage(nums,k))