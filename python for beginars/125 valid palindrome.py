class Solution :

    def isPalindrome(self, s):
     new_string = ""
     for i in s:
      if i.isalnum():
         new_string +=i.lower()
     return new_string ==new_string[::-1]     
solution = Solution()
s = "A man, a plan, a canal: Panama"
print(solution.isPalindrome(s))