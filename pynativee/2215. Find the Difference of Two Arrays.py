class Solution:
     def findDifference(self,nums1, nums2):
                n1 = []
                n2 = []
                nums2_set = set(nums2)
                nums1_set = set(nums1)
                for i in nums1:
                  if i not in nums2_set and i not in n1:
                    n1.append(i)
                for j in nums2:
                  if j not in nums1_set and j not in n2:
                        n2.append(j)
                return [n1]+[n2]
nums1 = [1,2,3,3]
nums2 = [1,1,2,2]      
sol = Solution()
print(sol.findDifference(nums1,nums2))