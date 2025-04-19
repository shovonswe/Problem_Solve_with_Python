class Solution:
    def groupAnagrams(self, strs):
        anargram_map = {}
        for word in strs:
            sorted_array = ''.join(sorted(word))
            if sorted_array in anargram_map:
                anargram_map[sorted_array].append(word)
            else:
                anargram_map[sorted_array] = [word]    
        return list(anargram_map.values())
Solution = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution.groupAnagrams(strs))    