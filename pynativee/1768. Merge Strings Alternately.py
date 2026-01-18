class Solution:
    def mergeAlternately(self, str, str1):
         new = []
         for i,j in zip(str, str1):
            new.append(i)
            new.append(j)
         new.append(str[len(str1):])
         new.append(str1[len(str):])
         return "".join(new)        
solution = Solution()
word1 = "abcd"
word2 = "pqr" 
print(solution.mergeAlternately(word1,word2))
