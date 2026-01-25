class Solution:
    def twoSum(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
solution = Solution()             
nums = [2, 3, 4,5, 6, 7]
target = 7
print(solution.twoSum(nums,target))