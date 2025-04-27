class Solution:
  def nextGreaterElement(self, nums1, nums2):
      stack = []
      nge = {}  # next greater element mapping

      for num in nums2:
          while stack and num > stack[-1]:
              nge[stack.pop()] = num
          stack.append(num)

      while stack:
          nge[stack.pop()] = -1

      ans = []
      for num in nums1:
          ans.append(nge[num])

      return ans
Solution = Solution()

nums1 =[1,3,5,2,4]
nums2 =[6,5,4,3,2,1,7]

print(Solution.nextGreaterElement(nums1,nums2))