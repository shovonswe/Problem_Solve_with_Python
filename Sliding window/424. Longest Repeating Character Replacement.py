#Optimal(Sliding_window)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        max_freq = 0
        max_len = 0
        
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            max_freq = max(max_freq, freq[s[right]])
            
            window_size = right - left + 1
            
            if window_size - max_freq > k:
                freq[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len
    
solution = Solution()
s = "ABAB"
k = 2
print(solution.characterReplacement(s,k))    



#Brute_force
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        max_len = 0
        
        for i in range(n):
            freq = {}
            max_freq = 0
            
            for j in range(i, n):
                freq[s[j]] = freq.get(s[j], 0) + 1
                max_freq = max(max_freq, freq[s[j]])
                
                window_size = j - i + 1
                
                if window_size - max_freq <= k:
                    max_len = max(max_len, window_size)
                else:
                    break
                    
        return max_len
solution = Solution()
s = "ABAB"
k = 2
print(solution.characterReplacement(s,k))