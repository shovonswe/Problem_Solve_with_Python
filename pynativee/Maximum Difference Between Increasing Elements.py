class Solution:
    def maximumDifference(self, nums):
        min_elements = float('inf')
        max_elements = 0
        
        for i in nums:
            min_elements = min(min_elements, i)  
            max_elements = max(max_elements, i - min_elements)  

        return max_elements


nums = [7, 1, 5, 3, 6, 4]
solution = Solution()
print(solution.maximumDifference(nums)) 
