class Solution:
    def longestCommonPrefix(self, strs):
        if not str:
         return ""
        prefix = strs[0] 
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
Solution = Solution()   
strs = ["flower","flow","flight"]    
print(Solution.longestCommonPrefix(strs))