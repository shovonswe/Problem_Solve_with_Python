class Solution:
    def merge(self, nums1, m, nums2, n):
        
        nums = []

        for i in range(m):
            nums.append(nums1[i])

        for j in range (n):
            nums.append(nums2[j])

       
        for i in range(m+n):

           nums1[i] = nums[i]   

        return sort.nums1() 
            


