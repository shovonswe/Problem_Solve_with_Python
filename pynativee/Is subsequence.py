class Solution:
 def isSubsequence(self,s,t):
    i = 0  # pointer for s
    for char in t:
        if i < len(s) and s[i] == char:
            i += 1
    return i == len(s)
Solution = Solution()
s="abc"
t="ahgbc"
print(Solution.isSubsequence(s,t))