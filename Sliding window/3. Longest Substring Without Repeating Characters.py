#optimal(Sliding_window)
class Solution:
    def lengthOfLongestSubstring(self, s):
        char_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len
solution = Solution()            
s = "pwwkew"
print(solution.lengthOfLongestSubstring(s))

#Brute Force.
class Solution:
      def lengthOfLongestSubstring(self, s):
            n = len(s)
            max_window = 0
            for i in range(n):
                  for  j in range(i+1,n+1):
                        r =s[i:j]
                  if len(r) == len(set(r)):     
                     max_window = max(len(r),max_window) 
            return max_window           

solution = Solution()            
s = "pwwkew"
print(solution.lengthOfLongestSubstring(s))
