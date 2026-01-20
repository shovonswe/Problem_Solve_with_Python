class Solution:
    def merge(self, nums1, m, nums2, n):
       
        nums1.sort()
        nums2.sort()

       
        valid_1 = nums1[-m:] if m > 0 else []
        valid_2 = nums2[-n:] if n > 0 else []

       
        merged = valid_1 + valid_2
        merged.sort()

       
        nums1.clear()
        nums1.extend(merged)


solution = Solution()

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

solution.merge(nums1, m, nums2, n)
print(nums1)
