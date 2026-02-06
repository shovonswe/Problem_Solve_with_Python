#Optimal(Sliding_window)
class Solution: 
      def maxVowels(self, s,k):
          vowel=set("aeiou")
          n = len(s)
          window = 0
          for i in range(k):
               if s[i] in vowel:
                    window += 1
          max_value = window
          for j in range(k,n):
               if s[j] in vowel :
                  window += 1
               if s[j-k] in vowel:
                    window -= 1
               max_value = max(window,max_value)
          return max_value                   
solution = Solution()
s = "abciiidef"
k = 3
print(solution.maxVowels(s,k))

#Brute_force
class Solution: 
      def maxVowels(self, s,k):
          vowel_ch = set("aeiou")
          #ch = list(s)
          n = len(s)
        
          max_value = 0
          for i in range(n-(k-1)):
               count = 0
               for j in range(i, i+k):
                    if s[j] in vowel_ch:
                         count += 1
               max_value = max(count,max_value)
          return max_value 
      
solution = Solution()
s = "abciiidef"
k = 3
print(solution.maxVowels(s,k))      