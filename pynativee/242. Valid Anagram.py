class Solution:

    def longest_unique_substring(self, s, t):
        s_count = {}
        t_count = {}
        for char_s in s:
            if char_s in s_count:
                s_count[char_s] += 1

            else:
                s_count[char_s] = 1

        for char_t in t:
            if char_t in t_count:
                t_count[char_t] += 1

            else:
                t_count[char_t] = 1
        if t_count == s_count:
            return True
        else:
            return False


Solution = Solution()
s = "rat"
t = "car"
print(Solution.longest_unique_substring(s, t))
