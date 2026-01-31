class Solution:
    def numSubseq(self, nums, target):
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)

        power = [1] * n
        for i in range(1, n):
            power[i] = (power[i-1] * 2) % MOD

        left, right = 0, n - 1
        ans = 0

        while left <= right:
            if nums[left] + nums[right] <= target:
                ans = (ans + power[right - left]) % MOD
                left += 1
            else:
                right -= 1

        return ans
solution = Solution ()
nums = [3,5,6,7]
target = 9
print(solution.numSubseq(nums,target))    