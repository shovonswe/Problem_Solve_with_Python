class Solution:
    def longestConsecutive(self, nums):
        num_set = nums
        long = 0
        for num in num_set:
            if num-1 not in num_set:
                current = 1
                streak = 1
            while current+1 in num_set:
                current += 1
                streak  +=1
            long = max(long,streak)        
        return long
Solution = Solution()
nums = [100,4,200,1,3,2]
print(Solution.longestConsecutive(nums))        