class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = {}
        for c in s:
          freq[c]  = freq.get(c,0)+1
        values = list(freq.values())
        return all(value == values[0] for value in values)

        

Solution = Solution()
print(Solution.areOccurrencesEqual("abacbc")) 
print(Solution.areOccurrencesEqual("aaabb"))  
