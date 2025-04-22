class Solution:
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        s_t = {}
        t_s = {}    
        for c1,c2 in zip(s,t):  
           if (c1 in s_t and s_t[c1] != c2) or( c2 in t_s and t_s[c2] != c1):
              return False
           s_t[c1] = c2
           t_s[c2] = c1
        return True
Solution = Solution()
s = "add"
t = "egg"
print(Solution.isIsomorphic(s,t))    